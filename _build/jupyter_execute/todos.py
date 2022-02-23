#!/usr/bin/env python
# coding: utf-8

# # Todo's en wensen

# ## Openen in Binder en in Jupyter Hub (i&i)
# 
# ```{todo} 
# **Openen in Binder en in Jupyter Hub (i&i)**
# 
# Deze inleiding in Jupyter en Jupyter Book moet links hebben voor het openen in Binder en voor het openen in Jupyter Hub, op de i&i hub. Dit laatste is voor het oefenen met de infrastructuur. Een gebruiker (docent) moet in het laatste geval wel een account hebben op deze hub.
# ```

# ## Wens: een extensie voor het bijhouden van vorderingen
# 
# Eén van de voordelen van Runestone Interactive is dat deze het mogelijk maakt voor een leerling om zijn vorderingen te zien - en voor een docent om de vorderingen van de leerlingen te zien.
# 
# Dit kunnen we alleen realiseren als we een dienst (server) waarop de leerling (en de docent) op de een of andere manier moet inloggen (hoeft niet onder de eigen naam).

# ## Tips voor het maken van lesmateriaal
# 
# We moeten een hoofdstuk (of meer) wijden aan tips voor het maken van lesmateriaal in het algemeen; en met behulp van Jupyter Book in het bijzonder.
# 
# We kunnen daarbij een opzet maken die door een docent zo als template overgenomen kan worden.

# ## Fout (in JB): navigatie onderaan de pagina
# 
# Deze navigatie moet netjes links en rechts staan; in de huidige versie staat deze alleen links. (Ik heb deze in een ander JB al eens aangepast?)

# ## Vertaling van admonitions
# 
# Jupyter Book (Sphinx) biedt allerlei "admonitions" voor tips, waarschuwingen e.d. in de tekst. Deze worden voorzien van een gekleurde kop met een icoontje.
# 
# In het Nederlandstalige materiaal willen we graag dat deze admonitions in het Nederlands vertaald worden. Bij voorkeur willen we zelf de vertaling bepalen; de "default" vertalingen zijn niet altijd geschikt.

# ## Jupyter games
# 
# * https://blog.jupyter.org/jupyter-games-cda20dc15a21

# ## Jupyter Lite - P5js?
# 
# Jupyter Lite is een versie van Jupyter die geheel in de browser uitgevoerd kan worden. Dit kan bijvoorbeeld gebruikt worden in combinatie met de P5js kernel.
# 
# * https://blog.jupyter.org/xeus-lite-379e96bb199d

# ## Interactieve slides
# 
# * gebruik van i&i Jupyter Hub (door docent)?
# * gebruik van MyBinder
# * via RISE
# * nog uitzoeken: via Voila?

# ---
# 
# ## DONE - onderstaande zijn al uitgevoerd

# ### Cell default - Markdown?
# 
# * https://stackoverflow.com/questions/40382454/jupyter-notebook-new-cell-type-default
# * onderstaande werkt, en is hier zo ingesteld.
# 
# In JupyterLab, you can go to Settings -> Advanced Settings manager -> Notebook and then add the following in "User Preferences":
# 
# ```
# {
#     "defaultCell": "markdown"
# }
# ```
