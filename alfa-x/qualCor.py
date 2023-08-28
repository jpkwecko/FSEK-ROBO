#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
from ajusteCor import *
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'




# ---------- Aqui é onde seus codigos começam

# ---------- Funções
corCS1 = 0
corCS2 = 0

def ajustes():
    global brancoMin
    global brancoMax
    global azulMin
    global azulMax
    global vermelhoMin
    global vermelhoMax
    global verdeMin
    global verdeMax
    global pretoMin
    global pretoMax
    global amareloMin
    global amareloMax
    global marromMin
    global marromMax
    global r, g, b

    print("Coloque no branco")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    brancoMin = (r-1, g-1, b-1)
    brancoMax = (r+1, g+1, b+1)
    print(brancoMin, brancoMax)
    time.sleep(5)

    print("Coloque no azul")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    azulMin = (r-1, g-1, b-1)
    azulMax = (r+1, g+1, b+1)
    print(azulMin, azulMax)
    time.sleep(5)
    
    print("Coloque no vermelho")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    vermelhoMin = (r-1, g-1, b-1)
    vermelhoMax = (r+1, g+1, b+1)
    print(vermelhoMin, vermelhoMax)
    time.sleep(5)

    print("Coloque no verde")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    verdeMin = (r-1, g-1, b-1)
    verdeMax = (r+1, g+1, b+1)
    print(verdeMin, verdeMax)
    time.sleep(5)

    print("Coloque no preto")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    pretoMin = (r-1, g-1, b-1)
    pretoMax = (r+1, g+1, b+1)
    print(pretoMin, pretoMax)
    time.sleep(5)

    print("Coloque no amarelo")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    amareloMin = (r-1, g-1, b-1)
    amareloMax = (r+1, g+1, b+1)
    print(amareloMin, amareloMax)
    time.sleep(5)

    print("Coloque no marrom")
    time.sleep(5)
    print(CS1.rgb)
    time.sleep(5)
    (r, g, b) = CS1.rgb
    marromMin = (r-1, g-1, b-1)
    marromMax = (r+1, g+1, b+1)
    print(marromMin, marromMax)
    time.sleep(5)

ajustes()
while True:
#def qualCor1():
    #global corCS1
    cor1 = CS1.rgb
    if (cor1 >= azulMin and cor1 <= azulMax):
        corCS1 = 2
    if (cor1 >= brancoMin and cor1 <= brancoMax):
        corCS1 = 6
    if (cor1 >= verdeMin and cor1 <= verdeMax):
        corCS1 = 3
    if (cor1 >= marromMin and cor1 <= marromMax):
        corCS1 = 7
    if (cor1 >= pretoMin and cor1 <= pretoMax):
        corCS1 = 1
    if (cor1 >= vermelhoMin and cor1 <= vermelhoMax):
        corCS1 = 5
    if (cor1 >= amareloMin and cor1 <= amareloMax):
        corCS1 = 4
    
#def qualCor2():
    #global corCS2
    #(r2, g2, b2) = (CS2.rgb)
    #if (r2 >= 40 and g2 >= 80 and b2 >= 60
    #    and r2 < 60 and g2 < 90 and b2 < 70):
    #    corCS2 = 2
    #if (r2 >= 225 and g2 >= 250 and b2 >= 150
    #    and r2 <= 255 and g2 <= 255 and b2 < 170):
    #    corCS2 = 6
    #if (r2 >= 50 and g2 >= 130 and b2 >= 35
    #    and r2 < 60 and g2 < 140 and b2 < 45):
    #    corCS2 = 3
    #if (r2 >= 70 and g2 >= 80 and b2 >= 25
    #    and r2 < 80 and g2 < 90 and b2 < 35):
    #    corCS2 = 7
    #if (r2 >= 35 and g2 >= 65 and b2 >= 20
    #    and r2 < 45 and g2 < 75 and b2 < 30):
    #    corCS2 = 1
    #if (r2 >= 200 and g2 >= 65 and b2 >= 20
    #    and r2 < 210 and g2 < 75 and b2 < 30):
    #    corCS2 = 5
    #if (r2 >= 215 and g2 >= 250 and b2 >= 40
    #    and r2 < 225 and g2 <= 255 and b2 < 50):
    #    corCS2 = 4

#while True:
    #qualCor1()
    #print(corCS1)
    #qualCor2()
    print(cor1)
    print(corCS1)