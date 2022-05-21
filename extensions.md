# Nuttige extensies

Omdat Jupyter Book gebaseerd is op Sphinx, kun je veel Sphinx extensies ook gebruiken voor Jupyter Book.
Enkele extensies zijn ingebouwd in Sphinx, deze kun je bijna direct gebruiken.

## Graphviz

Met Graphviz kun je diagrammen tekenen op basis van een tekst-gebaseerde beschrijving.
De volgende input ("digraph" staat voor *directed graph*):

```
:::{graphviz}
:align: center
digraph G {
  rankdir=LR
  node [shape=box, color=blue]
  stap1 -> stap2 -> stap3
}
:::

```

geeft het volgende resultaat:

:::{graphviz}
:align: center
digraph G {
  rankdir=LR
  node [shape=box, color=blue]
  stap1 -> stap2 -> stap3
}
:::

De documentatie en een groot aantal voorbeelden zijn te vinden op https://graphviz.org

Er zijn meer van dergelijke diagram-uitbreidingen, in verschillende variaties, voor verschillende soorten toepassingen.
Zie bijvoorbeeld het overzicht:

* https://blog.ouseful.info/2021/11/10/more-scripted-diagram-extensions-for-jupyter-notebook-sphinx-and-jupyter-book/
* https://blog.ouseful.info/2021/11/02/previewing-sphinx-and-jupyter-book-rendered-mermaid-and-wavedrom-diagrams-in-vs-code/
* https://blog.ouseful.info/2021/09/30/a-simple-pattern-for-embedding-third-party-javascript-generated-graphics-in-jupyter-notebools/
* https://opencomputinglab.github.io/SubjectMatterNotebooks/diagram/sphinx-diagrammers.html

In de auteursomgeving is graphviz al geïnstalleerd. Het is voldoende deze extensie aan de `_config`-settings toe te voegen, bijvoorbeeld:

```
sphinx:
  extra_extensions:
    - sphinx_exercise
    - sphinx.ext.graphviz
  config: 
    language: nl  
    graphviz_output_format: "svg"  
```

Hierin is als output-formaat SVG aangegeven; het default-formaat is PNG, dat is soms net wat minder "strak".

Om Graphviz te gebruiken op je computer moet je ook de bijbehorende software (het "dot" programma) installeren.
Zie hiervoor: https://graphviz.org/download/

## Todo

(over de todo-extensie)