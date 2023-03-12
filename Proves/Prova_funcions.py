import random
from tkinter import *
from PIL import Image, ImageTk


#Variables
llista = ["holaaa","adeu","casa",] 
vides = 0
guardades = set()

#Funcio element de la llista random
def aleatori():
    global paraula

    paraula = random.choice(llista)
    return "-" * len(paraula)

