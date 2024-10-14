import csv
from bs4 import BeautifulSoup

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