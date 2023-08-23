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

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'




# ---------- Aqui é onde seus codigos começam

# ---------- Funções
corCS1 = 0
corCS2 = 0


def qualCor1():
    global corCS1
    (r, g, b) = (CS1.rgb)
    if (r >= 35 and g >= 75 and b >= 45
        and r < 60 and g < 90 and b < 70):
        corCS1 = 2
    if (r >= 225 and g >= 250 and b >= 150
        and r <= 255 and g <= 255 and b < 170):
        corCS1 = 6
    if (r >= 50 and g >= 130 and b >= 35
        and r < 60 and g < 140 and b < 45):
        corCS1 = 3
    if (r >= 70 and g >= 80 and b >= 25
        and r < 80 and g < 90 and b < 35):
        corCS1 = 7
    if (r >= 35 and g >= 65 and b >= 20
        and r < 45 and g < 75 and b < 30):
        corCS1 = 1
    if (r >= 200 and g >= 65 and b >= 20
        and r < 210 and g < 75 and b < 30):
        corCS1 = 5
    if (r >= 215 and g >= 250 and b >= 40
        and r < 225 and g <= 255 and b < 50):
        corCS1 = 4
    
def qualCor2():
    global corCS2
    (r, g, b) = (CS2.rgb)
    if (r >= 40 and g >= 80 and b >= 60
        and r < 60 and g < 90 and b < 70):
        corCS2 = 2
    if (r >= 225 and g >= 250 and b >= 150
        and r <= 255 and g <= 255 and b < 170):
        corCS2 = 6
    if (r >= 50 and g >= 130 and b >= 35
        and r < 60 and g < 140 and b < 45):
        corCS2 = 3
    if (r >= 70 and g >= 80 and b >= 25
        and r < 80 and g < 90 and b < 35):
        corCS2 = 7
    if (r >= 35 and g >= 65 and b >= 20
        and r < 45 and g < 75 and b < 30):
        corCS2 = 1
    if (r >= 200 and g >= 65 and b >= 20
        and r < 210 and g < 75 and b < 30):
        corCS2 = 5
    if (r >= 215 and g >= 250 and b >= 40
        and r < 225 and g <= 255 and b < 50):
        corCS2 = 4