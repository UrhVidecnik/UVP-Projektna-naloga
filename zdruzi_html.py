def zdruzi_html_datoteke():
    with open("zdruzeni_html.html", "w", encoding='utf-8') as zdruzeno:
        for i in range(1, 10):
            with open(f"transfermarkt_stran_{i}.html", "r", encoding='utf-8') as datoteka:
                vsebina = datoteka.read()
                zdruzeno.write(vsebina)

    print("Vse HTML datoteke sem združil v datoteko 'zdruzeni_html.html'!")

zdruzi_html_datoteke()