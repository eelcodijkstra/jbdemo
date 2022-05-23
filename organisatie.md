# Organisatie van het materiaal

In dit gedeelte bespreken we een aantal richtlijnen voor de organisatie van het informatica-materiaal.
Het doel van deze richtlijnen is om het aanpassen van het materiaal voor een andere doelgroep relatief eenvoudig te maken.

* het is in Jupyter Book relatief eenvoudig om een hoofdstuk weg te laten of toe te voegen.
* in verband met verwijzingen vanuit elders is het in het algemeen handig om de structuur van een hoofdstuk zo goed mogelijk intact te laten; de nummering van de opdrachten e.d. blijft dan gelijk.
* 

## Voorbeeld: Physical computing

Het materiaal van Physical computing is beschikbaar in verschillende varianten: microbit-blokjeprogrammeren; Arduino-C++; en Lego Mindstorms. Het ligt voor de hand om een microbit-Python variant toe te voegen.

Een docent kiest voor een groep leerlingen een bepaalde variant. Het is niet handig als dit gemengd wordt met het materiaal van een andere variant.
Een deel van het materiaal is onafhankelijk van de gekozen variant. Je wilt dit gemeenschappelijke deel gemeenschappelijk  houden, en kopiëren zoveel mogelijk vermijden.

Omdat de publicatie-vorm gegenereerd wordt, kunnen we het gemeenschappelijke deel aan de input-zijde van het publicatieproces gelijk houden, terwijl de varianten in het resultaat met kopieën werken.

Gesuggereerde aanpak:

* de main branch in GitHub bevat het gemeenschappelijke deel
* de verschillende varianten zijn in de GitHub repo verschillende *branches*, 
    * deze branches zijn afgeleid van de main-branch, en bevatten ook het gemeenschappelijke deel
    * en hebben per branch daarnaast extra bestanden,
    * met per branch een eigen toc (table of contents)

## Enkele opmerkingen

We gebruiken meestal de volgende structuur, net als in dit boek:

```
format: jb-book
root: intro

parts:
- caption: Voorbeelden
  chapters:
  - file: voorbeelden
  - file: sqlite-2
  
- caption: Jupyter Notebook
  chapters:
  - file: jupyter-notebook
  
- caption: Jupyter Book
  chapters:
  - file: notebooks  
  - file: markdown
  - file: exercise
  - file: assessment

- caption: Infrastructuur
  chapters:
  - file: jb-infrastructuur
  - file: organisatie
  - file: extensions
    sections:
    - file: sphinx-assessment
    - file: sphinx-exercise
    - file: graphviz
  
- caption: Rest
  chapters:
  - file: over-dit-boek
  - file: todos
  - file: todolist



```

Een boek bestaat in dit geval uit *parts*; elk part heeft een aantal *chapters*; en elk chapter kan weer uit een aantal *sections* bestaan.

* (dat laatste zien we nog niet in dit voorbeeld...)

Zie voor meer uitleg over de table-of-contents structuur: https://jupyterbook.org/customize/toc.html

* meestal gebruiken we per hoofdstuk een inleiding, en losse files met de verschillende secties. In dat geval mag de inleiding geen extra kopjes gebruiken, alleen de hoofdstuk-titel. Je kunt bijv. gebruik maken van "rubric" als "titel".