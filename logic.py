import tensorflow as tf
from tensorflow import keras
import pandas as pd
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
from langdetect import detect


model = TFDistilBertForSequenceClassification.from_pretrained('model')
optimizer = keras.optimizers.Adam(learning_rate=5e-5)
model.compile(optimizer=optimizer, loss=model.hf_compute_loss, metrics=['accuracy'])
loaded_tokenizer = DistilBertTokenizer.from_pretrained('model')

    # Učitavanje podataka za treniranje i testiranje modela 
df_metadata = pd.read_json('News_Category_Dataset_v3.json', lines=True)
df = df_metadata.sample(n=100000, random_state=0)
df_out_of_sample = df_metadata[~df_metadata.isin(df)].dropna()

label_dict = {}
index = 0
for l in df.category.unique():
    label_dict[l] = index
    index += 1


def is_english(sentence):
    try:
        return detect(sentence) == 'en'
    except:
        return False
    

def contains_numbers(sentence):
    words = sentence.split()
    
    for word in words:
        if any(char.isdigit() for char in word):
            return True
    
    return False

def make_prediction(input_text):
    """
    Funkcija za pravljenje predikcije kategorije na osnovu unetog teksta.

    :param input_text: Tekst za koji se vrši predikcija.
    :return: Predikcija kategorije.
    """

    if(contains_numbers(input_text)):
        return False
    else:
        predict_input = loaded_tokenizer.encode(input_text,
            truncation=True,
            padding=True,
            return_tensors="tf")
    
        output = model(predict_input)[0]
        
        prediction_value = tf.argmax(output, axis=1).numpy()[0]
        pred_label = [d for d in label_dict if label_dict[d] == prediction_value][0]
        return pred_label


 