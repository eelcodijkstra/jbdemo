# Workflow: bestaand materiaal publiceren

In deze pagina beschrijven we hoe je als docent of auteur bestaand materiaal kunt aanpassen.
We gebruiken hiervoor dit Jupyter Book (*jbdemo*) als voorbeeld.

:::{admonition} Wat heb je nodig?

* een eigen GitHub account (dit is gratis; houd er rekening mee dat je deze account veel gebruikt, ook buiten de context van GitHub, bijvoorbeeld voor identificatie bij andere diensten.)
* een eigen account op de i&i Jupyter Hub voor auteurs.
* enige kennis van de Linux command-line
* enige kennis van Markdown 
:::


## Werken met bestaande content

Het lesmateriaal is in GitHub opgeslagen in de vorm van git(hub)-repositories.
Dit boek vind je op https://github.com/keuzethemas/jbdemo (zie ook het GitHub menu bovenin).

**1.** De eerste stap is om hiervan een eigen GitHub kopie ("fork") te maken.
Daarvan maak je een kopie ("clone") op de Jupyter Hub.
Met de Jupyter Book software genereer je de HTML-code daarvoor;
en tenslotte publiceer je deze op de Jupyter Hub als *statische website*.

Je kunt in de lokale kopie zonder risico wijzigingen aanbrengen: 
je kunt altijd weer de oorspronkelijke versie herstellen.

**2.** De volgende stap is om zelf het materiaal aan te passen of uit te breiden,
en deze wijzigingen op te slaan op GitHub.

**3.** De laatste stap is om een *pull request* te maken, om je eigen wijzigingen toe te voegen aan *jbdemo*.
Zo'n pull request wordt dan door de editors van de jbdemo-repository verwerkt (of voor kennisgeving aangenomen).

:::{graphviz}
:align: center

digraph {
    rankdir=TB
    node [shape=box, fontname="Gill Sans"]
    edge [fontname="Gill Sans"]
    ghk [label="GitHub\nkeuzethemas"]
    ghk -> ghh [label=" fork    "]
    ghh -> ghk [label="  pull request*"]
    ghh -> ghh [label="  create branch"]
    ghh [label="GitHub\nhans"]   
    jhh [label="Jupyter Hub\nhans"]
    ghh -> jhh [label="clone/fetch*  "  ]
    jhh -> jhh [label="  commit"]
    jhh -> ghh [label="  push*"]
}
:::

## Maak een GitHub *fork*

Zorg dat je (in de browser) ingelogd bent bij GitHub, en dat je op de pagina https://github.com/keuzethemas/jbdemo staat.
Je maakt nu een *fork* door op de fork-button rechtsboven te klikken, de gegevens in te vullen (of ingevuld te laten), en op de groene *Create Fork* button te klikken.

Als je naar je eigen account op GitHub gaat, zie je daar bij je repositories nu ook *jbdemo* staan.
Selecteer deze repository.
Je kunt de https-URL van je repository vinden onder de groene "Code" button.
Deze kun je kopiëren (Copy) door op de twee vierkantjes naast de URL te klikken.

## Maak een *clone* op Jupyter Hub

Zorg dat je ingelogd bent op de i&i Jupyter Hub: https://jupyter.infvo.nl.
In de Jupyter Lab UI zie je helemaal links het *git* icoon (niet het GitHub icoon), een gekanteld vierkantje met een "vorkje".
Klik daarop: als het goed is krijg je nu 3 blauwe knoppen; selecteer de onderste: *Clone a Repository*.
(Alternatief: gebruik het Git menu bovenin, en selecteer "clone repository".)
Vul (Paste) in het pop-up venster de https-URL van je repository in (na de Copy zoals hierboven beschreven).
Klik dan op de "Clone" button.

Je hebt nu een lokale clone (git-kopie) van je GitHub fork repository *jbdemo*.
Klik links boven op het "map" symbool. Als het goed is zie je nu bij je bestanden *jbdemo* staan.

## Genereer de HTML-code

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

Zorg dat je ingelogd bent op de Jupyter Hub.
In de Jupyter Lab UI zie je nu rechts een "launcher" tabblad staan.
(Mocht dat niet het geval zijn, dan voeg je via de blauwe "+" links boven een nieuwe launcher toe.)
Open hiermee een terminal-venster, door onderin op "Terminal" te klikken.
In deze terminal zie je de commando-regel waar je (linux) opdrachten kunt invoeren.
Geef de volgende opdracht:

```
jb build jbdemo
```

*NB* Deze opdracht veronderstelt dat je current working directory je home-directory is. Via de opdracht `cd` zonder argumenten kun je daar altijd naar terugkeren.)

Als het goed is wordt nu de HTML-code gegenereerd. Je krijgt allerlei meldingen op de terminal tijdens dit generatieproces. (Hopelijk geen foutmeldingen in dit geval.)
Aan het eind wordt gemeld dat je je boek via een lokale URL kunt vinden - maar die kun je helaas niet gebruiken.
Inplaats daarvoor hebben we de volgende stap nodig.

## Publiceer de HTML-code

Geef nu (na de vorige stap) de command-line opdracht:

```
jbpublish jbdemo
```

(`jbpublish` is één woord, zonder spatie.)

Als dit lukt, krijg je de URL te zien waar je je boek kunt vinden.
Kopieer die URL en open die in je browser, en controleer je boek online.
(**Let op: de URL eindigt op een `/`**).

## Maak lokaal een kleine wijziging

Zorg dat je in de Jupyter Lab UI bent, met links het venster met de bestanden van je home-directory.
Klik op de regel met *jbdemo*: je ziet dan de bestanden van het boek.
klik vervolgens op *intro.md*. Rechts verschijnt dan een edit-venster voor dit bestand.
Pas nu de titel bovenin aan, bijvoorbeeld: "Welkom bij het Jupyter Book van Hans".
Bewaar je wijziging (Command-S, of via het File menu link boven: Save Markdown File).
(Als er ongewijzigde wijzigingen zijn, zie je bovenin in de tab voor het edit-venster een zwart bolletje.
Als je alles bewaard hebt, wordt dit een kruisje, waarmee je de tab kunt sluiten.)

Selecteer de terminal-tab, en geef de opdrachten:

```
jb build jbdemo
jbpublish jbdemo
```

Controleer vervolgens je online gepubliceerde boek in de browser.

## Pas de inhoudsopgave aan

Zorg dat je in de Jupyter Lab UI bent, met links de bestanden van *jbdemo*.
Klik op *_toc.yml*.
Rechts opent nu een edit-venster voor de inhoudsopgave.
Zoek de regel met `  - file: kennismaking`.
Plaats aan het begin van deze regel een hekje (`#`) zodat dit commentaar wordt.
Bewaar je wijzigingen (Command-S, of menu File->Save YAML File)

Selecteer de terminal-tab, en geef de opdrachten:

```
jb build jbdemo
jbpublish jbdemo
```

Je krijgt nu een waarschuwing dat het bestand `kennismaking.md` niet in een table-of-contents gebruikt wordt (wat in dit geval de bedoeling is.)

Controleer de online versie in de browser: er is geen "kennismaking" meer in je boek.

:::{admonition} Over YAML bestanden
YAML-bestanden worden vaak gebruikt voor het beschrijven van een configuratie.
(Je kunt dit als de Python-variant van JSON zien.)
Dit formaat is goed te verwerken door computer en goed leesbaar voor mensen.
Let op: in een YAML-bestand is de *indentatie van belang*.
Een spatie te weinig of teveel geeft problemen.
:::

## Ruim alles weer op

Je kunt je wijziging op verschillende manieren ongedaan maken:

* via de *git* plugin
    * selecteer helemaal links de git-plugin (het gekantelde vierkantje)
    * selecteer op de regel *Changed* het linksom gebogen pijltje: Discard all changes.
    * NB: dit pijltje is pas zichtbaar als je cursor in die regel staat.
* via de commando-regel
    * verwijder alle *jbdemo* bestanden door:
    * `rm -rf jbdemo`
    * (je kunt altijd weer een lokale clone maken via git)
