# Organisatie van het materiaal

In dit gedeelte bespreken we een aantal richtlijnen voor de organisatie van het informatica-materiaal.
Het doel van deze richtlijnen is om het aanpassen van het materiaal voor een andere doelgroep relatief eenvoudig te maken.

* het is in Jupyter Book relatief eenvoudig om een hoofdstuk weg te laten of toe te voegen.
* in verband met verwijzingen vanuit elders is het in het algemeen handig om de structuur van een hoofdstuk zo goed mogelijk intact te laten; de nummering van de opdrachten e.d. blijft dan gelijk.

## Structuur van de inhoud

We gebruiken meestal een structuur met *parts*, *chapters* en *sections*, net als in dit boek:

```
format: jb-book
root: intro

parts:
- caption: Voorbeelden
  numbered: true
  chapters:
  - file: voorbeelden/voorbeelden
    sections:
    - file: voorbeelden/3_elm-list
    - file: voorbeelden/microbit-1b
    - file: voorbeelden/sqlite-2 

  - file: voorbeelden/overige
    sections:
    - file: voorbeelden/sphinx-vb
    - file: voorbeelden/mchoice-demo
    - file: voorbeelden/opdracht-demo  
    - file: voorbeelden/uitwerkingen
  
- caption: Jupyter Notebook
  numbered: true
  chapters:
  - file: jupyter-notebook
  
- caption: Jupyter Book
  numbered: true
  chapters:
  - file: notebooks  
  - file: markdown
  - file: sphinx-extensions/sphinx-extensions  
    sections:
    - file: sphinx-extensions/sphinx-exercise
    - file: sphinx-extensions/sphinx-assessment
    - file: sphinx-extensions/assessment  
    - file: sphinx-extensions/sphinx-graphviz
    - file: sphinx-extensions/sphinx-todo  

- caption: Infrastructuur
  numbered: true
  chapters:
  - file: jb-infrastructuur
  - file: organisatie

- caption: Rest
  chapters:
  - file: over-dit-boek
  - file: todos
  - file: todolist

```

Zie voor meer uitleg over de table-of-contents structuur: https://jupyterbook.org/customize/toc.html

:::{tip} 
In de bovenstaande aanpak heeft de inleiding van een hoofdstuk, zoals bijvoorbeeld "voorbeelden/voorbeelden.md",
alleen een "level 1" hoofdstuk-titel, en geen andere subtitels.
De section-bestanden beginnen met een "level 1" titel, en kunnen eventueel subtitels bevatten.
Op deze manier krijg je de hiërarchie en de nummering die je verwacht.

Als je in de inleiding een kopje nodig hebt, gebruik dan bijvoorbeeld een "rubric"-titel.
:::

### Organisatie van bestanden

Plaats alle bestanden van een hoofdstuk bij voorkeur in een aparte hoofdstuk-map.
Je kunt dan eenvoudig een hoofdstuk weglaten of toevoegen.
Figuren plaats je bij voorkeur in een sub-map *images*, zoals in het *voorbeelden*-hoofdstuk.

*Sphinx* plaatst alle figuren in de html-bestanden in een enkele map *images*:
je moet er dus voor zorgen dat de namen van de figuren in het hele document uniek zijn.

## Materiaal met varianten

Het materiaal voor Physical computing is beschikbaar in verschillende varianten: Arduino, Lego Mindstorms, en micro:bit.
Deze varianten hebben een deel van de bestanden gemeenschappelijk.
Een leerling werkt gewoonlijk maar aan één variant: deze wil het liefst een compleet document voor een bepaalde variant.

Omdat de publicatie-vorm gegenereerd wordt, kunnen we het gemeenschappelijke deel aan de input-zijde van het publicatieproces gelijk houden, terwijl de varianten in het resultaat met kopieën werken.

* combineer de bestanden voor alle varianten in één GitHub repo
* gebruik per variant een aparte inhoudsopgave (`_toc` bestand)
    * je kunt bij de "jb build" opdracht opgeven welk toc-bestand gebruikt moet worden.

### Voorbeeld: Physical computing

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