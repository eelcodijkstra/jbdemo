# Rest

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


## Eigen aanpassingen

* JH: maak een eigen *branch* (bijvoorbeeld met je naam, initialen) voor je eigen aanpassingen.
    * gebruik de *main* branch als uitgangspunt
* JH: 

## Werken met nieuwe (eigen) content

* GitHub: maak een *fork* van de template-repository


## Over git en GitHub

`git` is één van de meest gebruikte systemen voor versiebeheer. git is ontwikkeld door Linus Torvalds, de geestelijk van Linux.
``GitHub` is één van de meest gebruikte toepassingen voor het beheren van open source software: naast het bewaren van de source code in repositories biedt GitHub tegenwoordig ook mogelijkheden voor communicatie en project-organisatie.

Een git-repository bevat één of meer *branches*; de hoofd-branch is *main* (vroeger *master*).
Een branch bestaat uit een verzameling bestanden.
Een branch een geschiedenis van *commits*: elke commit bestaat uit een reeks wijzigingen in één of meer bestanden.

figuur: historie van een verzameling bestanden in git.

(We kunnen hiervan zelf een voorbeeld maken, op basis van de oefeningen van GitHub. Of, in het kader van onze eigen flow. Zie in GitHub: insights/network



De manier van werken is als volgt:

1. (GH) Je maakt *eenmalig* een fork in je GitHub account van de keuzethemas-repository (bijv. `jbdemo`).
2. (GH) Je maakt in die fork een branch voor je eigen werk, bijvoorbeeld onder je eigen naam (`hans`).
3. (JH) je maakt in Jupyter Hub een lokale *clone* van je fork in GitHub; zorg ervoor dat je eigen branch actief is.
4. (JH) je maakt lokaal wijzigingen in de bestanden; deze *commit* je in je eigen branch.
5. (JH) je *pusht* de lokale wijzigingen naar je GitHub fork.
6. (GH) indien nodig, maak je in GitHub een *pull request* van je eigen branch naar de main-branch van de originele repository.

Hierin staat (GH) voor acties die je in je online in je GitHub account uitvoert. (JH) staat voor acties die je op de i&i Jupyter Hub uitvoert.
De eerste 3 stappen voer je eenmaal uit. De laatste 3 stappen herhaal je zovaak als nodig is.

---


* bekijk de Jupyter Book inhoudsopgave (`_toc.yml`)
    * dit is een YAML-document: de indentatie heeft betekenis (als in Python)
* bekijk een Markdown-pagina (als "raw")