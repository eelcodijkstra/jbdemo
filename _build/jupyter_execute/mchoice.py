#!/usr/bin/env python
# coding: utf-8

# # Toetsvragen-demo

# Voor JupyterBook ontwikkelen we een extensie voor toetsvragen, in het bijzonder voor *formatief* toetsen in het lesmateriaal.
# 
# Je kunt de volgende toetsformaten gebruiken:
# 
# * multiple choice
# * drag & drop - plaats de juiste componenten bij elkaar
# * fillintheblank
# * Parsons' puzzels
# 
# Hieronder geven we een aantal voorbeelden. In de broncode van het Jupyter Notebook kun je ook zien hoe het formaat voor deze vragen eruit ziet.

# ## Multiple choice

# ```{mchoice} Vraag 1
# :correct: a
# 
# Welke van de onderstaande uitspraken is juist?
# 
# * het web is een toepassing van het internet
#     * Inderdaad
# * het internet is een toepassing van het web
#     * Lees de inleiding van "Netwerken" nog eens door
# * geen van beide
#     * Zie de inleiding van "Netwerken"
# 

# ```{mchoice} titel van de vraag
# :correct: c
# 
# Een mogelijk uitgebreide vraag, met figuren, formules, e.d.
# 
# De beschrijving van de vraag wordt afgesloten met een lijst van mogelijke antwoorden; bij elk antwoord is feedback mogelijk. 
# 
# * antwoord a
#     * feedbach bij antwoord a
# * antwoord b
#     * feedback bij antwoord b
# * antwoord c
#     * feedback bij antwoord c
# * antwoord d
#     * feedback bij antwoord d

# ## Drag & drop
# 
# Bij een drag&drop-vraag moeten elementen via drag and drop bij de bijbehorende elementen geplaatst worden, bijvoorbeeld een term bij een definie.
# 
# (Meestal gaan we ervan uit dat de linker elementen een kortere tekst hebben dan de rechter elementen.)

# ```{dragndrop} Landen en steden
# 
# Plaats de steden bij de landen.
# 
# **Let op!** Niet alle genoemde landen hebben een stad in de lijst; en niet alle steden hebben een land in de lijst.
# 
# * Nederland
#     * Amsterdam
#     * Dokkum
# * België
#     * Antwerpen
# * Verenigd Koninkrijk
# * no-target
#     * Dublin
# ```

# ## Fillintheblank
# 
# Bij een "fillintheblank" moet een antwoord gegeven worden dat in een opengelaten vakje past. Het antwoord kan een getal zijn of een string. Bij een getal kan gecontroleerd worden of dit in een bepaald bereik ligt. Een string kan gecontroleerd worden via een reguliere expressie.

# ```{fillintheblank} vraag 3
# 
# Het resultaat van `1 + 2 * 3` in Python is {blank-range}`7..7`.
# 
# Geef een voorbeeld van een Pascal identifier, met een selectie van letters, cijfers, en andere tekens {blank-regexp}`^[a-zA-Z][_0-9a-zA-Z]*$`
# 
# * 7
# * begint met een letter, dan letters, cijfers, of `_`
# ```
# 

# ## Parsons' puzzels
# 
# In een Parsons' puzzel moet je de regels van een programma in de goede volgorde plaatsen, met de juiste indentatie.
# 
# 

# ````{parsons} Vraag 5
# 
# Dit is de inleidende tekst.
# 
# Deze kan uit meerdere paragrafen bestaan. Dit voorbeeld betreft een (Python) programma om de getallen 0..9 af te drukken. 
# 
# Plaats de regels van het onderstaande programma in de juiste volgorde, met de juiste indentatie.
# 
# ```python
# x = 0
# while x < 10:
#     print(x)
#     x = x + 1
# ```
# 
# ````
