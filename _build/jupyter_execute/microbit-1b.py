#!/usr/bin/env python
# coding: utf-8

# # Microbit les 1b

# ````{panels}
# :header: bg-info text-white
# :card:
# 
# **Doel**
# ^^^
# Continu uitlezen van een analoge temperatuursensor en grafisch weergeven van de temperatuur.
# 
# ---
# 
# **Voorkennis**
# ^^^
# Les 01a-Temperatuur plotten
# 
# ````

# ````{panels}
# :card:
# 
# **Concepten**
# ^^^
# analoge temperatuursensor
# ---
# 
# **Wat heb je nodig?**
# ^^^
# microbit; "host" computer met Mu-editor
# breadboard; analoge temperatuursensor
# 
# ````

# ````{panels}
# :card:
# 
# **Schakeling**
# ^^^
# * sluit microbit-3V aan op Vcc van de sensor
# * sluit microbit-0V aan op Gnd van de sensor
# * sluit pin0 van de microbit aan op Out van de sensor
# 
# Zie breadboard-schakeling en schema verderop.
# ---
# 
# **LM35DZ pinout**
# ^^^
# ```{image} images/lm35dz-pinout.png
# :alt: lm35dz
# :class: bg-primary mb-1
# :width: 100px
# :align: center
# ```
# 
# ````

# ````{panels}
# :card:
# 
# **Analoge input**
# ^^^
# * `pin0.read_analog()`
# * resultaat: 0..1023
# * 0V=>0, 3.3V=>1023
# * 3.3V == 3300 mV
# 
# ---
# 
# **Karakteristieken LM35DZ**
# ^^^
# * temperatuur bereik 0-100 'C
# * nauwkeurigheid +/- 0.25 'C
# * 0 'C => 0V
# * 10 mV per 0.1 'C
# 
# ````

# ````{panels}
# :card:
# 
# **Python programma**
# ^^^
# ```python
# from microbit import *
# 
# while True:
#     temp1 = temperature()
#     temp2 = pin0.read_analog()
#     print((temp1, temp2))
#     sleep(100)
# ```
# 
# ---
# 
# **Nog aanpassen!**
# ^^^
# Het programma hiernaast in nog niet juist!
# 
# Voor het bepalen van `temp2` moet je rekening houden met:
# 
# * het spanningsbereik van de sensor, afhankelijk van de temperatuur;
# * het bereik van de A/D-omzetter van de microbit.
# 
# ````

# 
# 

# ````{list-table}
# :header-rows: 1
# 
# * - breadboard-schakeling
#   - schema
# * - ```{image} images/microbit-lm35_bb.png
#     :alt: lm35dz-breadboard
#     :class: bg-primary mb-1
#     :width: 400px
#     :align: center
#     ```
#   - ```{image} images/microbit-lm35_schem.png
#     :alt: lm35dz-schakeling
#     :class: bg-primary mb-1
#     :width: 400px
#     :align: center
#     ```
# ````
