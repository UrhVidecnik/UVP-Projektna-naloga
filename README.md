# SVETOVNA LESTVICA FIFA
**AVTOR:** Urh Videčnik

# Opis projektne naloge
Pri predmetu *Uvod v programiranje* sem moral narediti projektno nalogo. Projektna naloga je bila sestavljena iz 2 delov. 
Prvi del je bilo zajemanje podatkov s spletne strani, drugi del pa analiza pridobljenih podatkov. Za izdelavo projektne naloge sem uporabljal programski jezik **Python**.
Ker sem strastni navdušenec nogometa sem se odločil, da naredim analizo svetovne lestvice FIFA. Podatke sem pridobil s spletne strani [Transfermarkt.com](https://www.transfermarkt.com/).

Pobral sem podatke o:
- rankingu države,
- imenu države,
- številu članov,
- povprečni starosti igralcev,
- skupni vrednosti igralcev in
- točkah.

Nekaj držav ni imelo podatka o skupni vrednosti igralcev, zato sem to vrednost nadomestil z '-' kasneje pri izračunih pa sem to vrednosti pretvoril v '0 EUR'

# Navodila za uporabo programa
Končni izdelek moje projektne naloge si lahko uporabnik ogleda tako, da preprosto odpre datoteko **analiza.ipynb**. Podatki, ki jih je zajela analiza so iz datoteke **reprezentance.csv**, ki je pravtako vključena v reporzitoriju.

Če bi želel uporabnik sam zagnati program, oziroma osvežiti aktualne podatke, mora enostavno zagnati datoteko **glavna_koda.py**. Ta datoteka bo najprej s spletne strani [Transfermarkt.com](https://www.transfermarkt.com/) prenesla 9 html datotek, jih nato skupaj združila v eno html datoteko in na koncu vse skupaj zapisala v CSV datoteko.
Nazadnje pa mora pognati še datoteko analiza.ipynb, da se osvežijo aktualni podatki na grafih in v izračunih.