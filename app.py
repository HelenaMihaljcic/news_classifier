import tkinter as tk
from logic import make_prediction

def prikazi_kategoriju(unos_polje, rezultat_polje):
    """
    Funkcija koja se poziva prilikom pritiska na dugme za kategorizaciju teksta.

    Koristi make_prediction funkciju za dobijanje predikcije kategorije i prikazuje rezultat na ekranu.

    Args:
        unos_polje (tkinter.Entry): Polje za unos teksta.
        rezultat_polje (tkinter.Label): Polje za prikaz rezultata kategorizacije.
    """
    unos_teksta = unos_polje.get()  # Dobijanje teksta iz polja za unos
    rezultat_kategorizacije = make_prediction(unos_teksta)
    rezultat_polje.config(state=tk.NORMAL)  # Omogući pisanje u polje
    rezultat_polje.config(text=" ")  # Očisti prethodni rezultat
    rezultat_polje.config(text=rezultat_kategorizacije)
    rezultat_polje.config(state=tk.DISABLED)

def pokreni_aplikaciju(window):
    """
    Funkcija za kreiranje grafičkog korisničkog interfejsa.

    Args:
        window (tkinter.Window): Glavni prozor aplikacije.
    """
    window.title("Kategorizacija Teksta")
    window.geometry("700x400")
    window.configure(background='#ffffff')

    unos_labela = tk.Label(window, text="Unesite tekst", fg='#0f1847', font=('Arial', 12, 'bold'))
    unos_labela.pack(padx=10, pady=30)

    unos_polje = tk.Entry(window, width=70, font=('Arial', 10), bd=1, relief=tk.SOLID)
    unos_polje.pack(padx=10, pady=10)
    dugme_kategorizacija = tk.Button(window, text="Kategorizuj tekst", height=2, width=18, background='#0f1847', fg='white', font=('Arial', 12, 'bold'), command=lambda: prikazi_kategoriju(unos_polje, rezultat_polje), )
    dugme_kategorizacija.pack(pady=20)

    rezultat_polje = tk.Label(window, width=40, height=3, background="white", fg='black', font=('Arial', 12, 'bold'))
    rezultat_polje.pack(padx=10, pady=10)
    rezultat_polje.config(fg='white')
    window.mainloop()
