from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox

#Variables
vides = 6
guardades = set()
partides= 0

with open("Projecte_Final/llista.txt") as llista:
     llista = llista.read().splitlines()


#Funcio per canviar la imatge
def forca():
      global img
      img = Image.open("Projecte_Final/imatges/img"+str(vides)+".png")
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

      #Borrar contingut de guardades
      guardades = set()
      #Borrar contingut de eguions
      eguions.config(text="")
      #Borrar contingut de marcador_vides
      marcador_vides.config(text="Vides: "+str(vides))
      #Borrar contingut de marcador_lletra
      marcador_lletra.config(text="Lletres adivinades: "+str(guardades))
      #Borrar contingut de entrada
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
                        l2.config(image=imgG)
                        if messagebox.askretrycancel(message="¿Vols tornar ha intentar?", title="Has guanyat") == True:
                              reiniciar()
                        else:
                              win.destroy()

      else:
                  vides -= 1
                  if vides == 0:
                        l2.config(image=imgP)
                        eguions.config(text="La paraula era: "+paraula)
                  else:
                        forca()
      marcador_vides.config(text="Vides: "+str(vides))              
      marcador_lletra.config(text="Lletres adivinades: "+str(guardades))
      entrada.delete(0, END)


win = Tk()
win.geometry("700x400")
win.configure(bg = 'Orange')
win.title('PokePenjat')

defaultimg = Image.open("Projecte_Final/imatges/Inici.png")
defaultimg = defaultimg.resize((300, 200))
defaultimg = ImageTk.PhotoImage(defaultimg)

img_inici = Image.open("Projecte_Final/imatges/img6.png")
img_inici = img_inici.resize((200, 200))
img_inici = ImageTk.PhotoImage(img_inici)

imgG = Image.open("Projecte_Final/imatges/Guanyar.png")
imgG = imgG.resize((300, 200))
imgG = ImageTk.PhotoImage(imgG)

imgP = Image.open("Projecte_Final/imatges/Perdre.png")
imgP = imgP.resize((300, 200))
imgP = ImageTk.PhotoImage(imgP)

imgPK = Image.open("Projecte_Final/imatges/logoPK.png")
imgPK = imgPK.resize((200, 200))
imgPK = ImageTk.PhotoImage(imgPK)

l1 = Label(text="POKEPENJAT", background="Dark Blue", foreground="white", width=90, border= 10, anchor="center")
l1.place(x=0,y=0)

l2 = Label(image=defaultimg)
l2.place(x=50,y=50)

l3 = Label(image=imgPK)
l3.place(x=400,y=150)

eguions = Label(text="Paraula")
eguions.place(x=130,y=255)

entrada = Entry()
entrada.place(x=190,y=280, width=15)

marcador_vides = Label(text="Vides: "+str(vides), bg="Orange")
marcador_vides.place(x=400,y=50)

marcador_lletra = Label(text="Lletres adivinades: ", bg="Orange", wraplength=200)
marcador_lletra.place(x=400,y=90)

marcador_partides = Label(text="Partides jugades: ", bg="Orange")
marcador_partides.place(x=400,y=70)

#Botons
bcomençar = Button(text="Començar", command=començar)
bcomençar.place(x=135,y=310)
bsortir = Button(text="Sortir", command=win.destroy)
bsortir.place(x=250,y=310)
bjugar = Button(text="Jugar", command=comprovar)
bjugar.place(x=50,y=310)

win.mainloop()