# Verantwoording van keuze's

Bij het opzetten van de infrastructuur voor het Keuzethema's-materiaal hebben we een aantal keuze's gemaakt.
Deze betreffen de voorkeur voor het materiaal; het kan in voorkomende gevallen zinvol zijn om van deze voorkeuren af te wijken.

Belangrijke argumenten voor de keuze's zijn:

* continuïteit: de infrastructuur moet over 10 jaar (of langer) nog beschikbaar en up-to-date zijn (bijvoorbeeld met betrekking tot beveiliging);
* open source (waar mogelijk)
* waar mogelijk/zinvol, naast publicatie op het web, ook publicatie op PDF/papier (geheel of gedeeltelijk).
* de mogelijkheid voor docenten om een eigen afgeleide versie te maken
    * die up-to-date blijft met het origineel; en
    * waaruit bijdragen aan het origineel mogelijk zijn.
* versiebeheer: 

## Jupyter Notebook

Jupyter Notebook begint een belangrijk professioneel hulpmiddel te worden in de wereld van de Data Science, AI en gerelateerd onderzoek. Er is een grote en levendige community, die borg staat voor de *continuïteit* van deze infrastructuur.

Voor informatica-onderwijsmateriaal hebben deze Notebooks een aantal voordelen:

* de combinatie van lopende tekst en code-cellen maakt het mogelijk om interactieve voorbeelden te geven waar de lezer "mee kan spelen", door de code aan te passen en opnieuw uit te voeren;
* deze aanpak maakt het ook mogelijk om vrijwel elke vorm van *scaffolding* te bieden voor praktische (programmeer)opdrachten: van een compleet uitgewerkt voorbeeld tot een lege code-cell, met alle stappen daartussen.
* er zijn "kernels" voor een aantal onderwijs-programmeertalen beschikbaar: Python, Elm, SQL/SQLite, JavaScript (en p5.js: processing in JS).

## Jupyter Book

Een Jupyter Book combineert een aantal Notebooks en Markdown-bestanden tot een enkel "boek" dat via Sphinx in een publicatie-formaat omgezet wordt.
Sphinx is een systeem waarmee veel Python-gerelateerde documentatie (en documenten) gemaakt worden.
Hoewel dit meestal web-documenten zijn (html), maakt Sphinx het ook mogelijk om LaTex documenten aan te maken, voor publicatie als PDF. (*Voor ons materiaal werkt LaTeX-publicatie nog niet.*)

Jupyter Book is een onderdeel van het "executable books" project, waarmee boeken met interactieve code gepubliceerd kunnen worden.

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
