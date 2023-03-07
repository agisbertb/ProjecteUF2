import random
from tkinter import *
from PIL import Image, ImageTk


llista = [1,2,3,4,5,6,7,8,9,10]
vides = 6 
guardades=[]
#Funcio element de la llista random
def llistar(llista):
    return random.choice(llista)

#Forca depen de la vida
def forca(vides):
    global img

    img = Image.open("imatges/img"+str(vides)+".jpg")
    img = img.resize((400, 200))
    img = ImageTk.PhotoImage(img)

#Funcion guions
def guions(llistar):
    long = len(llistar)
    mult = '-' * long
    return mult

def comprovar(lletra,guardades):
    while True:
        if lletra in guardades:
            print("Has introduit una lletra repetida")
            print(guardades)
            continue
        else:
            break

 #Bucle hasta que ponga una letra
def bucle(a):
    while True:
        lletra = input("Introdueix una lletra: ")
        if len(lletra) == 1:
            print ("Has introduit una lletra")
            guardades.append(lletra)
       
        else:
            print ("Has introduit més d'una lletra")
            continue
        comprovar(lletra,guardades)



bucle()
