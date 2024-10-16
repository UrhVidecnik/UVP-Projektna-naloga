import requests
import http.client
from bs4 import BeautifulSoup
import csv

http.client._MAXHEADERS = 1000

glava = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

osnovni_url = "https://www.transfermarkt.com/wettbewerbe/fifa/wettbewerbe"

def prenesi_stran(stevilka_strani):
    url = f"{osnovni_url}?page={stevilka_strani}"
    odgovor = requests.get(url, headers=glava)
    vsebina = BeautifulSoup(odgovor.content, 'html.parser')
    with open(f"transfermarkt_stran_{stevilka_strani}.html", "w", encoding='utf-8') as datoteka:
        datoteka.write(vsebina.prettify())
    return vsebina

for i in range(1, 10):
    print(f"Prenašam stran {i}")
    prenesi_stran(i)

print("Vse strani so prenesene!")

def zdruzi_html_datoteke():
    with open("zdruzeni_html.html", "w", encoding='utf-8') as zdruzeno:
        for i in range(1, 10):
            with open(f"transfermarkt_stran_{i}.html", "r", encoding='utf-8') as datoteka:
                vsebina = datoteka.read()
                zdruzeno.write(vsebina)

    print("Vse HTML datoteke sem združil v datoteko 'zdruzeni_html.html'!")

zdruzi_html_datoteke()

with open("zdruzeni_html.html", "r", encoding="utf-8") as file:
    vsebina = file.read()

struktura = BeautifulSoup(vsebina, 'html.parser')

with open("reprezentance.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ranking države", "Narod", "Število članov", "Povprečna starost", "Skupna vrednost", "Točke"])
    vrstice = struktura.find_all('tr', {'class': ['odd', 'even']})
    
    for row in vrstice:
        ranking_drzave = row.find('td', {'class': 'zentriert cp'}).get_text(strip=True) if row.find('td', {'class': 'zentriert cp'}) else '-'

        narod = row.find('td', {'class': 'hauptlink'}).get_text(strip=True) if row.find('td', {'class': 'hauptlink'}) else '-'

        stevilo_clanov = row.find_all('td', {'class': 'zentriert'})[1].get_text(strip=True) if len(row.find_all('td', {'class': 'zentriert'})) > 1 else '-'

        povprecna_starost = row.find_all('td', {'class': 'zentriert'})[2].get_text(strip=True) if len(row.find_all('td', {'class': 'zentriert'})) > 2 else '-'

        skupna_vrednost = row.find('td', {'class': 'rechts'}).get_text(strip=True) if row.find('td', {'class': 'rechts'}) else '-'

        tocke = row.find_all('td', {'class': 'zentriert hauptlink'})[0].get_text(strip=True) if row.find_all('td', {'class': 'zentriert hauptlink'}) else '-'

        writer.writerow([ranking_drzave, narod, stevilo_clanov, povprecna_starost, skupna_vrednost, tocke])

print("Podatki so bili uspešno shranjeni v 'reprezentance.csv'!")