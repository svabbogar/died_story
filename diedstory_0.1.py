#author:Svab
#title:Died Story
#version:0.1
#date:2018.12.24.


#csomagok

import random


# Alap Statok
elet = int(0) #amennyi napot elt

egeszseg = int(100)
boldogsag = int(100)
nepszeruseg = int(100) # social life
penz = int(100) # random kezdes: nyomor, atlagos, luxus

# az esemeny ebbe a listaba fog kerulni, hogy ki lehessen irni

eletsztori = []



# par esemeny tesztelni

def lottonyeres():
    global boldogsag
    boldogsag = boldogsag + 20
    global penz
    penz = penz + 100
    eletsztori.append('-Megnyerte a lottot.')

def tuloratfizetnek():
    global penz
    penz = penz + 5
    global boldogsag
    boldogsag = boldogsag + 10
    eletsztori.append('-Kifizettek a tulorajat.')

def szocialissegely():
    global penz
    global boldogsag
    global nepszeruseg
    penz = penz + 4
    boldogsag = boldogsag + 2
    nepszeruseg = nepszeruseg - 5
    eletsztori.append('-Szocialis segelyt kapott.')

def penzttalalt():
    global penz
    global boldogsag
    penz = penz + 3
    boldogsag = boldogsag + 5
    eletsztori.append('-Penzt talalt.')

def penztorokolt():
    global penz
    global boldogsag
    global nepszeruseg
    penz = penz + 15
    boldogsag = boldogsag + 5
    nepszeruseg = nepszeruseg + 8
    eletsztori.append('-Penzt orokolt.')

def rokonoklatogatnak():
    global boldogsag
    boldogsag = boldogsag + 3
    eletsztori.append('-Meglatogattak a rokonai.')

def rokonodmeghal():
    global boldogsag
    global egeszseg
    boldogsag = boldogsag - 15
    egeszseg = egeszseg -2
    eletsztori.append('-Meghalt egy rokona.')



























#Ezt a listat kell meghivni, ebbe vannak a funkciok.

esemenyek = [lottonyeres, tuloratfizetnek, szocialissegely, penzttalalt, penztorokolt, rokonoklatogatnak, rokonodmeghal]




#jatek
while boldogsag > 0 or egeszseg > 0 or nepszeruseg > 0 or penz > 0:
    random.choice(esemenyek)()
    elet = elet+1

    if boldogsag < 1 or egeszseg < 1 or nepszeruseg < 1 or penz < 1:
        break
print('\n'.join(eletsztori))
print(str(elet), "napot elt.")
print('penz: '+str(penz), '\nboldogsag: '+str(boldogsag), '\negeszseg: '+str(egeszseg), '\nnepszeruseg: ', str(nepszeruseg))
