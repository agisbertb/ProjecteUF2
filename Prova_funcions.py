#Funcio elemento de la llista random
import random
from tkinter import *
from PIL import Image, ImageTk


llista = [1,2,3,4,5,6,7,8,9,10]

def llistar(llista):
    return random.choice(llista)


print(llistar(llista))
    
    