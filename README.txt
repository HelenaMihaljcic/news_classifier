# Kategorizacija Teksta

Ovaj program omogućuje kategorizaciju teksta koristeći prethodno trenirani model za klasifikaciju sekvenci. U ovom slučaju, koristi se DistilBERT model za klasifikaciju novinskih članaka po kategorijama.

## Instalacija i Pokretanje

1. Preporučuje se korištenje virtualnog okruženja kako bi se izolirale potrebne biblioteke za ovaj projekat. 
2. Instalirajte potrebne biblioteke naredbom: `pip install -r requirements.txt`.
3. Preuzmite prethodno trenirani model i tokenizer. Očekuje se da su model i tokenizer dostupni u direktoriju "model".
4. Preuzmite podatke za treniranje i testiranje modela. Očekuje se da je datoteka s podacima nazvana "News_Category_Dataset_v3.json" i da je dostupna u istom direktoriju kao i kod.
5. Pokrenite program naredbom: `python program.py`.

## Korištenje

1. Unesite tekst na engleskom jeziku koji želite kategorizirati u polje za unos teksta.
2. Pritisnite dugme "Kategorizuj tekst" kako biste vidjeli predikciju kategorije na osnovu unesenog teksta.
3. Rezultat kategorizacije će biti prikazan ispod polja za unos teksta.

## Struktura Koda

- `test.py`: Glavni programski kod koji sadrži funkcije za kategorizaciju teksta i grafičko korisničko sučelje pomoću biblioteke Tkinter.
- `requirements.txt`: Datoteka sa spiskom svih potrebnih biblioteka i njihovih verzija za ovaj projekat.
- `model/`: Direktorij koji sadrži prethodno trenirani model i tokenizer.

## Napomene

- Ovaj program koristi prethodno trenirani DistilBERT model za klasifikaciju teksta po kategorijama novinskih članaka.
- Predikcija kategorije se vrši na osnovu unesenog teksta koristeći model i tokenizer.
- Program koristi grafičko korisničko sučelje implementirano pomoću biblioteke Tkinter.

## Autor

Autor: Helena Mihaljčić