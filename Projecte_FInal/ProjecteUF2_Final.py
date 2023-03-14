from tkinter import *
from PIL import Image, ImageTk
import random

#Variables
llista = ["holaaa","adeu","casa",]
vides = 6
guardades = set()
partides= 0

#with open("llista.txt") as llista:
#      llista = llista.read().splitlines()


#Funcio per canviar la imatge
def forca():
      global img
      img = Image.open("imatges/img"+str(vides)+".png")
      img = img.resize((200, 200))
      img = ImageTk.PhotoImage(img)
      l2.config(image=img)
#Funcio element de la llista random
def aleatori():
    global paraula

    paraula = random.choice(llista)
    guions = "-" * len(paraula)
    eguions.config(text=guions)
#Funció per comenzar la partida
def començar():
      #Començar la partida
      l2.config(image=img_inici)
      aleatori()
#Funció per reiniciar la partida
def reiniciar():
      global guardades
      global partides
      global vides

      partides += 1
      vides = 6
      marcador_partides.config(text="Partides: "+str(partides)) 

      #Borrar contenido de guardades
      guardades = set()
      #Borrar contenido de eguions
      eguions.config(text="")
      #Borrar contenido de eresultat
      eresultat.config(text="")
      #Borrar contenido de marcador_vides
      marcador_vides.config(text="Vides: "+str(vides))
      #Borrar contenido de marcador_lletra
      marcador_lletra.config(text="Lletra adivinades: "+str(guardades))
      #Borrar contenido de entrada
      entrada.delete(0, END)
      l2.config(image=img_inici)
      aleatori()
#Funció per comprovar la entrada
def comprovar():
      global vides
      lletra = entrada.get()[0]
      bcomençar.config(text="Reiniciar", command=reiniciar)
#Guardar letra en guardades
      if lletra in guardades:
              return
      guardades.add(lletra)
#Comprovar si la lletra esta en la paraula
      if lletra in paraula:
                  for i in range(len(paraula)):
                        if paraula[i] == lletra:
                                    eguions.config(text=eguions.cget("text")[:i] + lletra + eguions.cget("text")[i+1:])
                  if "-" not in eguions.cget("text"):
                        eresultat.config(text="Has guanyat!")
                        l2.config(image=imgG)
                  else:
                        eresultat.config(text="Correcte")
      else:
                  vides -= 1
                  if vides == 0:
                        eresultat.config(text="Has perdut!")
                  else:
                        eresultat.config(text="Incorrecte")
                        forca()
                        eresultat.config(text="")
      marcador_vides.config(text="Vides: "+str(vides))              
      marcador_lletra.config(text="Lletra adivinades: "+str(guardades))
      entrada.delete(0, END)

win = Tk()
win.geometry("640x400")
win.configure(bg = 'yellow')
win.title('PokePenjat')

l1 = Label(text="Aplicació PenjAPP", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0,columnspan=2)

defaultimg = Image.open("imatges/Inici.png")
defaultimg = defaultimg.resize((300, 200))
defaultimg = ImageTk.PhotoImage(defaultimg)

img_inici = Image.open("imatges/img6.png")
img_inici = img_inici.resize((200, 200))
img_inici = ImageTk.PhotoImage(img_inici)

imgG = Image.open("imatges/Guanyar.png")
imgG = imgG.resize((200, 100))
imgG = ImageTk.PhotoImage(imgG)

l2 = Label(image=defaultimg)
l2.grid(column=0,row=1,columnspan=2)

eguions = Label(text="Paraula")
eguions.grid(column=0,row=2,columnspan=2)

eresultat = Label(text="Resultat")
eresultat.grid(column=0,row=6,columnspan=2)


entrada = Entry()
entrada.grid(column=0,row=3,columnspan=2)

marcador_vides = Label(text="Vides: "+str(vides))
marcador_vides.grid(column=0,row=7,sticky=E)

marcador_lletra = Label(text="Lletres adivinades: ")
marcador_lletra.grid(column=0,row=8,sticky=W)

marcador_partides = Label(text="Partides jugades: ")
marcador_partides.grid(column=0,row=9,sticky=W)

#Botons
bcomençar = Button(text="Començar", command=començar)
bcomençar.grid(column=0,row=4,sticky=E)
bsortir = Button(text="Sortir", command=win.destroy)
bsortir.grid(column=0,row=4,sticky=W)
bjugar = Button(text="Jugar", command=comprovar)
bjugar.grid(column=0,row=5,sticky=W)

win.mainloop()