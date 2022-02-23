#!/usr/bin/env python
# coding: utf-8

# # Voorbeelden - Sphinx layout

# ## Admonitions
# 
# Voor waarschuwingen, tips, e.d. zijn er speciale "admonition" blokken, met een gekleurde rand en titel.
# Voor elk soort betekenis is er een speciale kleur en icon.
# 
# Voorbeelden:

# :::{note}
# Dit is een opmerking. Door de vormgeving krijgt deze extra aandacht.
# :::
# 
# :::{warning}
# Dit is een waarschuwing.
# :::
# 
# Deze admonition-blokken worden ook gebruikt voor opdrachten en toetsvragen.

# ## Sphinx panels
# 
# * https://sphinx-panels.readthedocs.io
# * de panels hebben hier een schaduwrand; gebruik het`:card:` attribuut om deze schaduw weg te laten.

# ````{panels}
# 
# Panel header 1
# ^^^
# Panel body 1
# +++
# Panel footer 1
# ---
# 
# Panel header 2
# ^^^
# Panel body 2
# +++
# Panel footer 2
# ````

# ## Aantekeningen in de marge

# ```{margin} Marginal note
# Dit is een aantekening in de marge.
# Deze illustreert de tekst hiernaast.
# ```

# Een bekende stijl voor (les)boeken is het gebruik van aantekeningen in de marge (marginal notes). Deze stijl wordt onder meer gebruikt in Feynmann's Lectures on Physics. Edward Tufte maakt hiervan ook graag gebruik.
# 
# Dit is één van de stijlen die door Jupyter Book direct ondersteund wordt. Zie: https://jupyterbook.org/content/layout.html

# ## Zijbalk-elementen

# ```{sidebar} Verbanden zijn belangrijk
# Voor het onthouden en verwerken van nieuwe concepten zijn verbanden met andere concepten die je al eerder gezien hebt van belang. In een zijbalk (sidebar) kun je dergelijke verbanden aangeven zonder de lijn van het lopende verhaal te onderbreken.
# 
# Je kunt daarvoor aantekeningen in de marge gebruiken, of een zijbalk, zoals hier.
# ```

# Een ander veel gebruikt element is de zijbalk: een toelichting of voorbeeld bij de lopende tekst, niet direct van belang voor het volgen van de lijn van het verhaal. Je kunt hier bijvoorbeeld een verband met een ander onderwerp aangeven.
# 
# In het algemeen is een zijbalk groter en opvallender. Deze trekt soms meer aandacht dan de lopende tekst.

# ```{div} full-width
# 
# **Opmerking:** inhoud over de volle breedte werkt (kennelijk) niet bij zijbalken.
# 
# ---
# 
# (full width content)
# ```
