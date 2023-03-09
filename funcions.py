import random
from tkinter import *
from PIL import Image, ImageTk

#Variables
llista = ["holaaa","adeu","casa",] 
vides = 1
guardades = []
lletra = "a"


#Funcio element de la llista random
def llistar(llista):
    return random.choice(llista)
aleatori = llistar(llista)

#Comprovar si la lletra esta guardada
def comprovar(lletra,guardades):
    while True:
        if lletra in guardades:
            print("Has introduit una lletra repetida")
            print(guardades)
            continue
        else:
            break

 #Bucle hasta que ponga una letra
def bucle(lletra):
    while True:
        lletra = input("Introdueix una lletra: ")
        if len(lletra) == 1:
            break
        else:
            print("Has introduit mes d'una lletra")
            continue

#Demana una lletra i la guarda
def demanar(lletra):
    bucle(lletra)
    guardades.append(lletra)
    return guardades

