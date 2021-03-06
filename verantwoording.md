# Verantwoording van keuze's

Bij het opzetten van de infrastructuur voor het Keuzethema's-materiaal hebben we een aantal keuze's gemaakt.
Deze betreffen de voorkeur voor het materiaal; het kan in voorkomende gevallen zinvol zijn om van deze voorkeuren af te wijken.

Belangrijke argumenten voor de keuze's zijn:

* de didactische mogelijkheden, in het bijzonder voor informatica-onderwijs
* continuïteit: de infrastructuur moet over 10 jaar (of langer) nog beschikbaar en up-to-date zijn (bijvoorbeeld met betrekking tot beveiliging);
* open source (waar mogelijk)
* waar mogelijk/zinvol, naast publicatie op het web, ook publicatie op PDF/papier (geheel of gedeeltelijk).
* de mogelijkheid voor docenten om een eigen afgeleide versie te maken
    * die up-to-date blijft met het origineel; en
    * waaruit bijdragen aan het origineel mogelijk zijn.
* versiebeheer: 
* het gebruik van "platte tekst" waar mogelijk en zinvol
    * dit geeft de meeste mogelijkheden voor automatische verwerking, incl. versiebeheer

## Jupyter Notebook

Jupyter Notebook (https://jupyter.org) is een veel gebruikt hulpmiddel voor o.a. Data Science onderzoekers, voor het uitvoeren van onderzoek en voor het publiceren van de resultaten.
Andere onderzoekers kunnen het oorspronkelijke onderzoek daarmee herhalen en analyseren.
Jupyter Notebook vormt zo een belangrijke stap naar Open Research.

Voor het onderwijs biedt de combinatie van tekst en uitvoerbare code veel mogelijkheden. Zie bijvoorbeeld: 

* [Teaching and learning with Jupyter](https://jupyter4edu.github.io/jupyter-edu-book/)
* https://www.epfl.ch/education/educational-initiatives/cede/digitaltools/jupyter-notebooks-for-education/
* https://www.surf.nl/jupyter-notebook-toegankelijke-en-interactieve-data-analyse-voor-onderzoek-en-onderwijs


Jupyter Notebook werkt als een web-applicatie: gebruikers hoeven geen software te installeren.

Jupyter Notebook begint een belangrijk professioneel hulpmiddel te worden in de wereld van de Data Science, AI en gerelateerd onderzoek. Er is een grote en levendige community, die borg staat voor de *continuïteit* van deze infrastructuur.

Voor informatica-onderwijsmateriaal hebben deze Notebooks een aantal voordelen:

* de combinatie van lopende tekst en code-cellen maakt het mogelijk om interactieve voorbeelden te geven waar de lezer "mee kan spelen", door de code aan te passen en opnieuw uit te voeren;
* deze aanpak maakt het ook mogelijk om vrijwel elke vorm van *scaffolding* te bieden voor praktische (programmeer)opdrachten: van een compleet uitgewerkt voorbeeld tot een lege code-cell, met alle stappen daartussen.
* er zijn "kernels" voor een aantal onderwijs-programmeertalen beschikbaar: Python, Elm, SQL/SQLite, JavaScript (en p5.js: processing in JS).

## Jupyter Book

Een Jupyter Book combineert een aantal Notebooks en Markdown-bestanden tot een enkel "boek" dat via Sphinx in een publicatie-formaat omgezet wordt.
Sphinx is een systeem waarmee veel Python-gerelateerde documentatie (en documenten) gemaakt worden.
Hoewel dit meestal web-documenten zijn (html), maakt Sphinx het ook mogelijk om LaTex documenten aan te maken, voor publicatie als PDF. (*Voor ons materiaal werkt LaTeX-publicatie nog niet.*)

Jupyter Book biedt, door het bundelen van Jupyter Notebooks en Markdown documenten, een volgende stap voor het gebruik van Jupyter Notebooks in het onderwijs.
De [executable books website](https://executablebooks.org/en/latest/gallery.html) bevat een grote reeks voorbeelden van onderwijsmateriaal gemaakt met Jupyter Book en Jupyter Notebooks.

Zowel Jupyter, Sphinx als Jupyter Book zijn open source projecten, met een grote en levendige community.

:::{graphviz}
:align: center
digraph G {
  rankdir=LR
  node [shape=box]
  mdfile [label="Markdown files"]
  jnfile [label="Notebook files"]
  toc [label="_toc file"]
  config [label="_config file"]
  jbook [shape=ellipse, label="jb build"]
  sphinx [shape=ellipse, label=Sphinx]
  
  mdfile -> jbook -> sphinx -> HTML
  jnfile -> jbook
  toc -> jbook
  config ->jbook
  sphinx -> PDF
}
:::

## GitHub

Voor versiebeheer is in de informatica "git" eigenlijk de standaard.
GitHub is een van de belangrijkste infrastructuren voor open-source software.
Bovendien is GitHub, door het gebruik van de website en van GitHub Desktop, vrij gemakkelijk te gebruiken (ten opzichte van git op de command line).
Een aantal informatica-docenten gebruikt GitHub in de klas, bijvoorbeeld via GitHub Classroom (https://classroom.github.com).
Kennis van git en van GitHub is voor informatica-docenten eigenlijk een "must"; dan ligt het gebruik daarvan in de keuzethemas-infrastructuur voor de hand.

> GitHub voldoet niet aan de eis van "open source": GitHub is tegenwoordig onderdeel van Microsoft. Gezien het belang van GitHub voor de open source community is dit geen probleem voor de continuïteit.

Een belangrijk aspect van *git* is dat er geen fundamenteel onderscheid is tussen het origineel van een repository en een "clone" daarvan. Elke clone of fork bevat een complete kopie van het origineel, met de volledige historie daarvan. (In het proces maak je wel onderscheid tussen het origineel en een kopie, maar dat is puur voor het proces.)

