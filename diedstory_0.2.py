#author:Svab
#title:Died Story
#version:0.2
#date:2018.12.25.


#csomagok
import time
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
    global egeszseg
    egeszseg = egeszseg + 1
    boldogsag = boldogsag + 20
    global penz
    penz = penz + 100
    eletsztori.append('-Megnyerte a lottot.')

def tuloratfizetnek():
    global egeszseg
    egeszseg = egeszseg + 1
    global penz
    penz = penz + 5
    global boldogsag
    boldogsag = boldogsag + 10
    eletsztori.append('-Kifizettek a tulorajat.')

def szocialissegely():
    global egeszseg
    egeszseg = egeszseg + 1
    global penz
    global boldogsag
    global nepszeruseg
    penz = penz + 4
    boldogsag = boldogsag + 2
    nepszeruseg = nepszeruseg - 5
    eletsztori.append('-Szocialis segelyt kapott.')

def penzttalalt():
    global egeszseg
    egeszseg = egeszseg + 1
    global penz
    global boldogsag
    penz = penz + 3
    boldogsag = boldogsag + 5
    eletsztori.append('-Penzt talalt.')

def penztorokolt():
    global egeszseg
    egeszseg = egeszseg + 1
    global penz
    global boldogsag
    global nepszeruseg
    penz = penz + 15
    boldogsag = boldogsag + 5
    nepszeruseg = nepszeruseg + 8
    eletsztori.append('-Penzt orokolt.')

def rokonoklatogatnak():
    global egeszseg
    egeszseg = egeszseg + 1
    global boldogsag
    boldogsag = boldogsag + 3
    eletsztori.append('-Meglatogattak a rokonai.')

def rokonodmeghal():
    global egeszseg
    egeszseg = egeszseg + 1
    global boldogsag
    boldogsag = boldogsag - 15
    eletsztori.append('-Meghalt egy rokona.')

def kozelihozzatartozohalala():
    global egeszseg
    egeszseg = egeszseg + 1
    global boldogsag
    boldogsag = boldogsag - 15
    eletsztori.append('-Meghalt egy kozeli hozzatartozoja.')

def csaladinap():
    global egeszseg
    egeszseg = egeszseg + 1
    global boldogsag
    global penz
    boldogsag = boldogsag + 4
    penz = penz - 2
    eletsztori.append('-Meghalt egy kozeli hozzatartozoja.')

def baratno():
    global egeszseg
    egeszseg = egeszseg + 1
    global boldogsag
    global penz
    boldogsag = boldogsag + 4
    penz = penz - 10
    eletsztori.append('-Volt egy baratnoje.')

def egyejszakas_okes():
    global penz
    global nepszeruseg
    global egeszseg
    egeszseg = egeszseg - 1
    penz = penz - 2
    nepszeruseg = nepszeruseg + 3
    eletsztori.append('-Egyejszakas kalandban volt resze.')

def egyejszakas_beteg():
    global penz
    global nepszeruseg
    global egeszseg
    penz = penz - 2
    nepszeruseg = nepszeruseg + 3
    egeszseg = egeszseg - 6
    eletsztori.append('-Egyejszakas kalandban volt resze, de nem vedekezett jol. Nemi beteg lett.')

def kocsma_egyedul():
    global penz
    global egeszseg
    global nepszeruseg
    penz = penz - 1
    egeszseg = egeszseg - 1
    nepszeruseg = nepszeruseg + 1
    eletsztori.append('-Elment kocsmazni..')

def kocsma_haverokkal():
    global penz
    global egeszseg
    penz = penz - 1
    egeszseg = egeszseg - 2
    eletsztori.append('-Elment kocsmazni a haverjaival.')

def kocsma_tealltad():
    global egeszseg
    egeszseg = egeszseg - 1
    global penz
    global nepszeruseg
    penz = penz - 4
    nepszeruseg = nepszeruseg + 3
    eletsztori.append('-Elment kocsmazni es o allt egy kort.')

def kocsma_meghivtak():
    global egeszseg
    egeszseg = egeszseg - 1
    global nepszeruseg
    nepszeruseg = nepszeruseg + 2
    eletsztori.append('-Elment kocsmazni es meghivtak pialni.')

def megfazas_kis():
    global egeszseg
    egeszseg = egeszseg - 1
    eletsztori.append('-Kicsit megfazott...')

def megfazas_nagy():
    global egeszseg
    egeszseg = egeszseg - 2
    eletsztori.append('-Nagyon megfazott csorikam..')

def etkezes_egeszseges():
    global egeszseg
    egeszseg = egeszseg + 2
    global penz
    penz = penz - 2
    eletsztori.append('-Ma egeszsegesen etkezett.')

















#Ezt a listat kell meghivni, ebbe vannak a funkciok.

esemenyek = [lottonyeres, tuloratfizetnek, szocialissegely, penzttalalt, penztorokolt,
             rokonoklatogatnak, rokonodmeghal, kozelihozzatartozohalala, csaladinap,
             baratno, egyejszakas_okes, egyejszakas_beteg, kocsma_egyedul, kocsma_tealltad,
             kocsma_meghivtak, megfazas_kis, megfazas_nagy, etkezes_egeszseges]




#jatek
while boldogsag > 0 or egeszseg > 0 or nepszeruseg > 0 or penz > 0:
    random.choice(esemenyek)()
    elet = elet+1

    if boldogsag > 100:
        boldogsag = boldogsag-(boldogsag-100)
    if egeszseg > 100:
        egeszseg = egeszseg-(egeszseg-100)
    if penz > 200:
        penz = penz-(penz-200)
    if nepszeruseg > 100:
        nepszeruseg = nepszeruseg-(nepszeruseg-100)

    if boldogsag < 1 or egeszseg < 1 or nepszeruseg < 1 or penz < 1:
        break
print('\n'.join(eletsztori))
print(str(elet), "napot elt.")
print('penz: '+str(penz), '\nboldogsag: '+str(boldogsag), '\negeszseg: '+str(egeszseg), '\nnepszeruseg: ', str(nepszeruseg))
time.sleep(10)
