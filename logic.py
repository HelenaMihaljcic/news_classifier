import tensorflow as tf
import string
import enchant as enchant
from tensorflow import keras
import pandas as pd
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification

# Učitavanje prethodno treniranog modela i tokenizer-a
model = TFDistilBertForSequenceClassification.from_pretrained('model')
optimizer = keras.optimizers.Adam(learning_rate=5e-5)
model.compile(optimizer=optimizer, loss=model.hf_compute_loss, metrics=['accuracy'])
loaded_tokenizer = DistilBertTokenizer.from_pretrained('model')

# Učitavanje podataka za treniranje i testiranje modela
df_metadata = pd.read_json('News_Category_Dataset_v3.json', lines=True)
df = df_metadata.sample(n=100000, random_state=0)
df_out_of_sample = df_metadata[~df_metadata.isin(df)].dropna()

# Kreiranje rječnika za mapiranje kategorija na brojeve
label_dict = {}
index = 0
for l in df.category.unique():
    label_dict[l] = index
    index += 1


def contains_elements(word):
    """
    Provjerava da li data riječ sadrži neki od znakova interpunkcije.

    Args:
        word (str): Riječ koja se provjerava.

    Returns:
        element(char): Ako riječ sadrži znak interpunkcije vraća taj znak, u suprotnom vraća " "
    """

    non_letters = string.punctuation + string.whitespace
    
    for element in non_letters:
        if element in word:
            return element
            
    return " "


def validate_text(input_text):
    """
    Provjerava da li su sve riječi u tekstu ispravno napisane prema engleskom jeziku.

    Args:
        input_text (str): Tekst koji se provjerava.

    Returns:
        bool: True ako su sve riječi ispravno napisane, False ako barem jedna riječ nije ispravno napisana.
    """
    d = enchant.Dict("en_US")

  
    words_old = input_text.split()
    words = list(filter(bool, words_old))

    for word in words:

        symbol = contains_elements(word)
        if(symbol != " "):
            new_words = word.split(symbol)
            filter_words = list(filter(bool, new_words))

            for new_word in filter_words:
                words.append(new_word)

            continue

        # Provjera samo ako je riječ neprazna i sadrži samo slova
        if d.check(word) is False:
            return False

    return True



def make_prediction(input_text):
    """
    Funkcija za pravljenje predikcije kategorije na osnovu unetog teksta.

    Args:
        input_text (str): Tekst za koji se vrši predikcija.

    Returns: 
        pred_label (str) : Predikcija kategorije ili poruka o greški.
    """

    if(validate_text(input_text)):

        predict_input = loaded_tokenizer.encode(input_text,
            truncation=True,
            padding=True,
            return_tensors="tf")

        output = model(predict_input)[0]

        prediction_value = tf.argmax(output, axis=1).numpy()[0]
        pred_label = [d for d in label_dict if label_dict[d] == prediction_value][0]

    else:
        pred_label = "Tekst sadrži nedozvoljene riječi!"

    return pred_label