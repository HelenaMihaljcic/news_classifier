import tensorflow as tf
from tensorflow import keras
import pandas as pd
from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
from termcolor import colored
import tkinter as tk

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

def make_prediction(input_text):
    """
    Funkcija za pravljenje predikcije kategorije na osnovu unijetog teksta.

    :param input_text: Tekst za koji se vrši predikcija.
    :return: Predikcija kategorije.
    """
    predict_input = loaded_tokenizer.encode(input_text,
        truncation=True,
        padding=True,
        return_tensors="tf")

    output = model(predict_input)[0]

    prediction_value = tf.argmax(output, axis=1).numpy()[0]
    pred_label = [d for d in label_dict if label_dict[d] == prediction_value][0]
    return pred_label

def prikazi_kategoriju():
    """
    Funkcija koja se poziva prilikom pritiska na dugme za kategorizaciju teksta.

    Koristi make_prediction funkciju za dobijanje predikcije kategorije i prikazuje rezultat na ekranu.
    """
    unos_teksta = unos_polje.get()  # Dobijanje teksta iz polja za unos
    rezultat_kategorizacije = make_prediction(unos_teksta)
    rezultat_polje.config(state=tk.NORMAL)  # Omogući pisanje u polje
    rezultat_polje.config(text=" ")  # Očisti prethodni rezultat
    rezultat_polje.config(text="Kategorija " + rezultat_kategorizacije)
    rezultat_polje.config(state=tk.DISABLED)

if __name__ == "__main__":
    # Kreiranje glavnog prozora
    window = tk.Tk() 
    window.title("Kategorizacija Teksta")
    window.geometry("400x400")
    window.configure(background = "#2f024d")


    unos_labela = tk.Label(window)
    unos_labela.setvar("Unesite tekst")
    unos_labela.config(fg='white')
    
    # Dodavanje polja za unos teksta  
    unos_polje = tk.Entry(window, width=40)
    unos_polje.pack(padx=10, pady=100)

    # Dodavanje dugmeta za pokretanje kategorizacije
    dugme_kategorizacija = tk.Button(window, text="Kategorizuj tekst", command=prikazi_kategoriju)
    dugme_kategorizacija.pack(pady=5)

    # Dodavanje polja za prikaz rezultata
    rezultat_polje = tk.Label(window, width=40, height=3, background="#2f024d")
    rezultat_polje.pack(padx=10, pady=10)
    rezultat_polje.config(fg='white')

    # Pokrenitanje glavne petlje
    window.mainloop()
 
