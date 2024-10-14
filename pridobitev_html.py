import requests
import http.client
from bs4 import BeautifulSoup

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