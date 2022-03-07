# Welkom bij de Jupyter Book demo



Voor het lesmateriaal van de Informatica keuzethema's willen we gebruik maken van Jupyter en Jupyter Book.
Het eerste gedeelte bevat een aantal  voorbeelden hoe het resultaat eruit zou kunnen zien.
Voor de meeste gebruikers (docenten) is dit een handige eerste stap.

Het tweede gedeelte gaat over Jupyter Notebook. Een Jupyter Book bestaat uit een verzameling Jupyter Notebooks: in het algemeen, een notebook per web-pagina. Een notebook bevat vaak een combinatie van tekst en code, bijvoorbeeld in Python. Als lezer (leerling) kun je het notebook van een pagina activeren om interactief met de code-inhoud aan de slag te gaan. Dit is relevant voor alle docenten en leerlingen.

Het derde deel bevat een inleiding in Jupyter Book: welke mogelijkheden heb je om het materiaal vorm te geven? Dit is van belang voor auteurs en voor docenten die het materiaal willen aanpassen - bijvoorbeeld om een eigen versie voor hun leerlingen te maken.

Het vierde deel bevat een overzicht van de auteursomgeving: de verschillende interfaces en hulpmiddelen om van Jupyter Notebooks tot een gepubliceerd Jupyter Book te komen.

In het vijfde deel geven we een aantal overwegingen die tot de keuze voor dit platform geleid hebben. Ook geven we aan welke ontwikkelingen we in de toekomst nog verwachten.

````{panels}

{ref}`Voorbeelden <toetsvragen_demo>`
^^^
Voorbeelden o.a. uit keuzethema's lesmateriaal vormgegeven met Jupyter Book.
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

VB-FIG

:::{note}
...note...
:::

And here is a code block:

```
e = mc^2
```

Check out the content pages bundled with this sample book to see more.
