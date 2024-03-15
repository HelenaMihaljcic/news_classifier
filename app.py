import tkinter as tk
from logic import model, loaded_tokenizer, make_prediction




def prikazi_kategoriju():
    """
    Funkcija koja se poziva prilikom pritiska na dugme za kategorizaciju teksta.

    Koristi make_prediction funkciju za dobijanje predikcije kategorije i prikazuje rezultat na ekranu.
    """
    unos_teksta = unos_polje.get()  # Dobijanje teksta iz polja za unos

    rezultat_kategorizacije = make_prediction(unos_teksta)

    if(rezultat_kategorizacije == False):
        rezultat_polje.config(state=tk.NORMAL)  # Omogući pisanje u polje
        rezultat_polje.config(text=" ")  # Očisti prethodni rezultat
        rezultat_polje.config(text="NEKOREKTAN UNOS!")
        rezultat_polje.config(state=tk.DISABLED)
    else:
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