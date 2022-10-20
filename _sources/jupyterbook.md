# Over Jupyter Book

Met Jupyter Book kun je Markdown (MyST) bestanden en Jupyter Notebooks combineren tot één "boek" dat in verschillende formaten gepubliceerd kan worden: online, als HTML; of als PDF, wat eventueel op papier afgedrukt kan worden. *(Deze laatste optie is momenteel voor het keuzethema's materiaal helaas nog niet beschikbaar.)*

:::{margin}
*Jupyter Book* is onderdeel van het *Executable books project*.
:::

Zowel in het Markdown-formaat als in Jupyter Notebooks kun je gebruik maken van uitvoerbare code-cellen, waarmee je een *interactief executeerbaar boek* krijgt.
Dit maakt het erg geschikt voor informatica-onderwijs.

:::{graphviz}
:align: center
:caption: De Jupyter Book keten

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

## MyST Markdown

In een MySt Notebook kun je de Sphinx extensions gebruiken, zoals sphinx-exercises en sphinx-assessment.

Als je extra metadata toevoegt dan kun je ook "executable code cells" gebruiken die uitgevoerd worden als in een Jupyter Notebook. Dit heb je alleen nodig als je interactieve cellen op je pagina wilt hebben.

## Jupyter Notebook

Jupyter Book maakt het gebruik van MyST Markdown mogelijk in een Jupyter Notebook.
Dit betekent dat je voor de tekst-elementen in het notebook veel meer mogelijkheden hebt dan de standaard Markdown.

## Sphinx extensions

Jupyter Book maakt gebruik van Sphinx: dit betekent dat Shpinx-extensions ook bruikbaar zijn voor Jupyter Book.
Enkele nuttige extensions voor gebruik in het onderwijs zijn `sphinx-exercise` (ontwikkeld voor Jupyter Book) en `sphinx-assessment` (ontwikkeld voor het i&i lesmateriaal).
