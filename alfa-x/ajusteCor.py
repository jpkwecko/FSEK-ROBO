#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
import colorsys
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 

CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'

brancoMin = 0, 0, 0
brancoMax = 0, 0, 0
azulMin = 0, 0, 0
azulMax = 0, 0, 0
vermelhoMin = 0, 0, 0
vermelhoMax = 0, 0, 0
verdeMin = 0, 0, 0
verdeMax = 0, 0, 0
pretoMin = 0, 0, 0
pretoMax = 0, 0, 0
amareloMin = 0, 0, 0
amareloMax = 0, 0, 0
marromMin = 0, 0, 0
marromMax = 0, 0, 0
(r, g, b) = 0, 0, 0

# ---------- Aqui é onde seus codigos começam

# ---------- Funções
#def ajustes():
#    global brancoMin
#    global brancoMax
#    global azulMin
#    global azulMax
#    global vermelhoMin
#    global vermelhoMax
#    global verdeMin
#    global verdeMax
#    global pretoMin
#    global pretoMax
#    global amareloMin
#    global amareloMax
#    global marromMin
#    global marromMax
#    global r, g, b
#
#    print("Coloque no branco")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    brancoMin = (r-5, g-5, b-5)
#    brancoMax = (r+5, g+5, b+5)
#    print(brancoMin, brancoMax)
#    time.sleep(5)
#
#    print("Coloque no azul")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    azulMin = (r-5, g-5, b-5)
#    azulMax = (r+5, g+5, b+5)
#    print(azulMin, azulMax)
#    time.sleep(5)
#    
#    print("Coloque no vermelho")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    vermelhoMin = (r-5, g-5, b-5)
#    vermelhoMax = (r+5, g+5, b+5)
#    print(vermelhoMin, vermelhoMax)
#    time.sleep(5)
#
#    print("Coloque no verde")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    verdeMin = (r-5, g-5, b-5)
#    verdeMax = (r+5, g+5, b+5)
#    print(verdeMin, verdeMax)
#    time.sleep(5)
#
#    print("Coloque no preto")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    pretoMin = (r-5, g-5, b-5)
#    pretoMax = (r+5, g+5, b+5)
#    print(pretoMin, pretoMax)
#    time.sleep(5)
#
#    print("Coloque no amarelo")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    amareloMin = (r-5, g-5, b-5)
#    amareloMax = (r+5, g+5, b+5)
#    print(amareloMin, amareloMax)
#    time.sleep(5)
#
#    print("Coloque no marrom")
#    time.sleep(5)
#    print(CS1.rgb)
#    time.sleep(5)
#    (r, g, b) = CS1.rgb
#    marromMin = (r-5, g-5, b-5)
#    marromMax = (r+5, g+5, b+5)
#    print(marromMin, marromMax)
#    time.sleep(5)