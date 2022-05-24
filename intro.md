# Welkom bij de Jupyter Book demo

Dit *Jupyter Book* bevat een demonstratie en uitleg van het gebruik van Jupyter Notebooks en Jupyter Book voor het publiceren van het informatica *keuzethema's* materiaal.
Daarnaast beschrijft dit boek de infrastructuur die i&i opgezet heeft voor docenten/auteurs.

````{panels}

{ref}`Voorbeelden <voorbeeld-paginas>`
^^^
Voorbeelden uit het keuzethema-lesmateriaal vormgegeven met Jupyter Book.

* {ref}`Functioneel programmeren: Elm voorbeeld <Elm-voorbeeld>`
* {ref}`Physical computing: microbit opdracht <microbit-1b>`
* {ref}`Databases: SQL join <sqlite-2>`
---

Jupyter Notebook
^^^
Een notebook combineert opgemaakte tekst met code-cellen die de lezer kan uitvoeren en aanpassen.
````

````{panels}

{ref}`Jupyter Book <jupyter_book>`
^^^
Jupyter Book combineert een aantal notebooks tot een boek. MyST Markdown geeft extra mogelijkheden voor de opmaak.
---

{ref}`Auteursomgeving <jb_infrastructuur>`
^^^
De infrastructuur en hulpmiddelen om van een reeks Notebooks een gepubliceerd Jupyter Book te maken.
````

````{panels}

{ref}`Oefeningen<sphinx-exercise>`
^^^
Het de oefeningen-extensie kun je opdrachten formuleren en de uitwerkingen beschrijven.
---

{ref}`Toetsvragen<sphinx-assessment>`
^^^
Met de toetsvragen-extensie kun je allerlei soorten toetsvragen formuleren,
bijvoorbeeld multiple choice, drag-&-drop, Parsons, fill-in-the-blank.
````

Een Jupyter Book is een "boek" gemaakt uit een reeks Jupyter notebooks.
In de meeste gevallen gebruik je zo'n boek online, vanwege de interactieve mogelijkheden.
Het is ook mogelijk om het boek om te zetten in PDF's die je kunt afdrukken.

* wat is Jupyter Notebook?
* waarom Jupyter Notebook voor (informatica) onderwijs?
    * mogelijkheden voor interactie, in het bijzonder bij programmeeropdrachten
    * mogelijkheden voor scaffolding; combinatie van uitleg en code
    * aansluiten bij belangrijke ontwikkeling in o.a. Data Science (grote & professionele community)
* wat is Jupyter Book?
    * combineren van reeks notebooks
    * uitgebreidere versie van MarkDown, met meer opmaak-mogelijkheden
    * (gebaseerd op Sphinx en docutils, gebruikt voor allerlei documentatie, vooral in de Python-context - zie bijv. readthedocs; en: mogelijkheden voor plugins)
    * Sphinx plugins: https://github.com/yoloseem/awesome-sphinxdoc#extensions
* waarom Jupyter Book voor (informatica) onderwijs?
    * organiseren van het onderwijsmateriaal op basis van Jupyter Notebooks
    * speciale uitbreidingen
* speciale uitbreidingen voor Jupyter Book
* het gebruik van Jupyter Book in je onderwijs
* het aanpassen van Jupyter Book voor eigen gebruik
* de i&i Jupyter Book - ontwikkelomgeving
* alternatieven
    * Runestone Interactive (te specifiek)
    * (wat is er mis met Word?)
* begrippenlijst (glossary)
    
## Wat is Jupyter?

Een Jupyter Notebook is een combinatie van (opgemaakte) tekst met uitvoerbare programmacode.
De tekst geeft gewoonlijk een uitleg van een probleem en van de aanpak van de oplossing,
waarbij deze oplossing in de programmacode uitgewerkt is.

Een Notebook bestaat uit een reeks cellen: een cel bevat of opgemaakte tekst, of programmacode.
De cellen met programmacode kunnen zowel afzonderlijk als opeenvolgend uitgevoerd worden.

FIG notebook

Jupyter Notebooks zijn oorspronkelijk veel gebruikt voor onderzoek in Data Science,
zowel voor het daadwerkelijke onderzoek als voor het publiceren van de resultaten daarvan.
In een Notebook kunnen dan zowel de eigenlijke publicatie, de data, en de gebruikte programmacode gecombineerd worden.
Het onderzoek is daardoor helemaal transparant en herhaalbaar.

Een voorbeeld van een dergelijke publicatie is: (met een FIG)

Oorspronkelijk begonnen als iPython, is Jupyter tegenwoordig met veel meer programmeertalen te gebruiken.
Naast Python zijn er bijvoorbeeld "kernels" voor ....., Elm (functioneel programmeren), SQLite (database queries).


## Waarom Jupyter voor het informatica-onderwijs?

Door de combinatie van tekst voor de uitleg en uitvoerbare programmacode kun je direct het verband tussen theorie en praktijk leggen.
Voor programmeeronderwijs heeft Jupyter bovendien het voordeel dat je veel mogelijkheden hebt voor *schaffolding*.
Je kunt beginnen met uitgewerkte voorbeelden, waarover vragen beantwoord moeten worden.
Een stap verder is het geven van half-uitgewerkte voorbeelden waarin nog een paar elementen ingevuld moeten worden.
En tenslotte kun je grotere blokken programmacode laten ontwikkelen.

VB-FIG

Deze code kan steeds in de context van het Jupyter Notebook uitgevoerd en getest worden. De directe feedback helpt daarbij om misverstanden vroegtijdig te signaleren.

In Jupyter Book kunnen we deze elementen ook nog combineren met interactieve toetsvragen, bijvoorbeeld Multiple Choice vragen, invulvragen, of "Parsons' puzzles" voor programmeren.
