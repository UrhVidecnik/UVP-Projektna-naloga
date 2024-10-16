import requests
import http.client
from bs4 import BeautifulSoup
import csv
# vse knjižnice, ki sem jih potreboval

http.client._MAXHEADERS = 1000 

glava = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# Nastavitev glave, da se predstavi kot običajen spletni brskalnik in s tem prepreči blokiranje

osnovni_url = "https://www.transfermarkt.com/wettbewerbe/fifa/wettbewerbe"  # URL, s katerim sem nalagal HTML


def prenesi_stran(stevilka_strani): # Funkcija za prenos posamezne strani
    url = f"{osnovni_url}?page={stevilka_strani}"
    odgovor = requests.get(url, headers=glava) 
    vsebina = BeautifulSoup(odgovor.content, 'html.parser')
    
    
    with open(f"transfermarkt_stran_{stevilka_strani}.html", "w", encoding='utf-8') as datoteka: # Shranjuje razčlenjeno HTML vsebino v datoteko z ustreznim imenom za posamezno stran
        datoteka.write(vsebina.prettify())  # Preoblikuje HTML v lepo oblikovano besedilo in ga shrani
    
    return vsebina


for i in range(1, 10): # Zanka za prenos prvih 9 strani
    print(f"Prenašam stran {i}")  # Izpiše številko strani, ki se prenaša
    prenesi_stran(i)

print("Vse strani so prenesene!")  # Sporočilo po koncu prenosa vseh strani


def zdruzi_html_datoteke(): # Funkcija, ki združi prenesene HTML datoteke v eno datoteko
    with open("zdruzeni_html.html", "w", encoding='utf-8') as zdruzeno:
        for i in range(1, 10):
            with open(f"transfermarkt_stran_{i}.html", "r", encoding='utf-8') as datoteka:
                vsebina = datoteka.read()  # Prebere vsebino posamezne datoteke
                zdruzeno.write(vsebina)  # Zapiše prebrano vsebino v združeno datoteko

    print("Vse HTML datoteke sem združil v datoteko 'zdruzeni_html.html'!")  # Sporočilo po koncu združevanja

zdruzi_html_datoteke()

with open("zdruzeni_html.html", "r", encoding="utf-8") as file: # Odpira združeno HTML datoteko za branje.
    vsebina = file.read()  # Prebere vsebino združene HTML datoteke

struktura = BeautifulSoup(vsebina, 'html.parser')  # Razčleni združeno HTML datoteko z uporabo BeautifulSoup

with open("reprezentance.csv", "w", newline="", encoding="utf-8") as csvfile: # Odpira novo CSV datoteko za zapisovanje podatkov
    writer = csv.writer(csvfile)
    
    writer.writerow(["Ranking države", "Narod", "Število članov", "Povprečna starost", "Skupna vrednost", "Točke"])  # Zapiše vrstico z imeni stolpcev v CSV datoteko
    
    vrstice = struktura.find_all('tr', {'class': ['odd', 'even']}) # Najde vse vrstice tabele, ki vsebujejo podatke (razredi 'odd' in 'even' za izmenične vrstice).
    
    for row in vrstice:     # Zanka za obdelavo vsake vrstice
        # Poišče in pridobi besedilo za različne stolpce (če ne obstaja, doda '-').
        ranking_drzave = row.find('td', {'class': 'zentriert cp'}).get_text(strip=True) if row.find('td', {'class': 'zentriert cp'}) else '-'

        narod = row.find('td', {'class': 'hauptlink'}).get_text(strip=True) if row.find('td', {'class': 'hauptlink'}) else '-'

        stevilo_clanov = row.find_all('td', {'class': 'zentriert'})[1].get_text(strip=True) if len(row.find_all('td', {'class': 'zentriert'})) > 1 else '-'

        povprecna_starost = row.find_all('td', {'class': 'zentriert'})[2].get_text(strip=True) if len(row.find_all('td', {'class': 'zentriert'})) > 2 else '-'

        skupna_vrednost = row.find('td', {'class': 'rechts'}).get_text(strip=True) if row.find('td', {'class': 'rechts'}) else '-'

        tocke = row.find_all('td', {'class': 'zentriert hauptlink'})[0].get_text(strip=True) if row.find_all('td', {'class': 'zentriert hauptlink'}) else '-'

        writer.writerow([ranking_drzave, narod, stevilo_clanov, povprecna_starost, skupna_vrednost, tocke]) # Zapiše vse podatke o ekipi v CSV datoteko.


print("Podatki so bili uspešno shranjeni v 'reprezentance.csv'!")  # Sporočilo po uspešnem zapisu podatkov v CSV datoteko
