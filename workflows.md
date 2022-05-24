# Workflows

## Werken met bestaande content

Het lesmateriaal is in GitHub opgeslagen in de vorm van git(hub)-repositories.
We geven hieronder een voorbeeld hoe je aan de slag kunt gaan met bestaand materiaal.
We gebruiken dit boek ("jbdemo") als voorbeeld.

De eerste stap is het zelf publiceren van het bestaande materiaal,
om de publicatie workflow te begrijpen.
Je kunt in de lokale kopie zonder risico wijzigingen aanbrengen: 
je kunt altijd weer de oorspronkelijke versie herstellen.

De volgende stap is om zelf het materiaal aan te passen of uit te breiden,
en deze wijzigingen op te slaan op GitHub.

De laatste stap is om een "pull request" te maken, om je eigen wijzigingen toe te voegen aan *jbdemo*.

:::{admonition} Wat heb je nodig?

* een eigen GitHub account (dit is gratis; houd er rekening mee dat je deze account veel gebruikt, ook buiten de context van GitHub, bijvoorbeeld voor identificatie bij andere diensten.)
* een eigen account op de i&i Jupyter Hub voor auteurs.
* enige kennis van de Linux command-line
* enige kennis van Markdown
:::

### De Jupyter Book publicatie-flow

* GitHub: maak een eigen *fork* van de bestaande `jbdemo` repository.
* JL: maak een *clone* van je eigen fork.

"GitHub" staat hier voor GitHub, ingelogd op je eigen account.
"JL" staat hier voor Jupyter Lab, ingelogd op je eigen account op de i&i Jupyter Hub voor auteurs.

Je hebt nu de bestanden van *jbdemo* op je eigen account op Jupyter Hub staan.

* JL: start een terminal-venster op 

Je geeft deze commando's op de *command line* in een *termimal*-venster. 

:::{graphviz}
:align: center
:caption: Jupyter Book flow
:name: jb-flow-fig

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

* JL: commando `jb build jbdemo`
* JL: commando `jb-publish jbdemo`

:::{admonition} Opdracht: pas een bestand aan

* Open het bestand xxx met Jupyter Lab (double-click op de naam van het bestand links).
* Breng een kleine verandering aan en bewaar het bestand (CTRL-S of CMD-S)
* Bouw de gewijzigde versie: `jb build jbdemo`
* publiceer deze: `publish jbdemo`
* en bekijk deze versie: https://jupyter/infvo.nl/books/hans/jbdemo/
    * waarin je `hans` vervangt door je eigen *username*
    * vergeet de laatste `/` niet!
:::    

:::{admonition} Opdracht: pas de inhoudsopgave aan

* Open het bestand `_toc.yml` met Jupyter Lab (double-click op de naam van het bestand links).
* Zet het commentaar-teken `#` aan het begin van de regel `. file: verantwoording`. Je verwijdert daarmee (tijdelijk) dit bestand uit de inhoud. Bewaar het bestand (CTRL-S of CMD-S)
* Bouw de gewijzigde versie: `jb build jbdemo`
* publiceer deze: `publish jbdemo`
* en bekijk deze versie: https://jupyter/infvo.nl/books/hans/jbdemo/
    * waarin je `hans` vervangt door je eigen *username*
    * vergeet de laatste `/` niet!
::: 

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