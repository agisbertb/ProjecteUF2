from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from keyboard import *


#Variables
vides = 6
guardades = set()
partides= 0
r, g, b,a = 236,54,61,255


with open("llista.txt") as llista:
     llista = llista.read().splitlines()

#Funcio per limitar la entrada a una lletra
def limit_input(text):
    if len(text) > 1:
        return False
    return True

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
    eguions.config(text=guions, font=("Garamond", 15, "bold"))
#Funció per comenzar la partida
def començar():
      #Començar la partida
      global partides
      partides += 1
      marcador_partides.config(text="Partides jugades: "+str(partides)) 
      l2.config(image=img_inici)
      aleatori()
#Funció per reiniciar la partida
def reiniciar():
      global guardades
      global partides
      global vides

      partides += 1
      vides = 6
      marcador_partides.config(text="Partides jugades: "+str(partides)) 

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
def comprovar(*args):
      global vides
      lletra = entrada.get()[0]
      bcomençar.config(text="Reiniciar", command=reiniciar)
      
#Guardar letra en guardades
      if lletra in guardades:
            messagebox.showwarning(message="Ja has introduit la lletra "+lletra+"\n""introdueïx una altra lletra", title="Lletra introduida")
            entrada.delete(0, END)
            return      
      guardades.add(lletra)
#Comprovar si la lletra esta en la paraula
      if lletra in paraula:
                  for i in range(len(paraula)):
                        if paraula[i] == lletra:
                                    eguions.config(text=eguions.cget("text")[:i] + lletra + eguions.cget("text")[i+1:], font=("Garamond", 15, "bold"))
                  if "-" not in eguions.cget("text"):
                        l2.config(image=imgG)
                        if messagebox.askyesno(message="¿Vols tornar ha jugar?", title="Has guanyat") == True:
                              reiniciar()
                        else:
                              win.destroy()
      else:
                  vides -= 1
                  if vides == 0:
                        l2.config(image=imgP)
                        if messagebox.askyesno(message="La paraula era "+paraula+", Vols tornar ha jugar?", title="Has perdut") == True:
                              reiniciar()
                        else:
                              win.destroy()
                  else:
                        forca()
      marcador_vides.config(text="Vides: "+str(vides), font=("Garamond", 10, "bold"))              
      marcador_lletra.config(text="Lletres utilitzades: "+str(guardades), font=("Garamond", 10, "bold"))
      entrada.delete(0, END)

win = Tk()
win.geometry("700x400")
win.configure(bg = "#ec363d")
win.title('PokePenjat')

defaultimg = Image.open("imatges/Inici.png")
defaultimg = defaultimg.resize((300, 200))
defaultimg = ImageTk.PhotoImage(defaultimg)

img_inici = Image.open("imatges/img6.png")
img_inici = img_inici.resize((200, 200))
img_inici = ImageTk.PhotoImage(img_inici)

imgG = Image.open("imatges/Guanyar.png")
imgG = imgG.resize((300, 200))
imgG = ImageTk.PhotoImage(imgG)

imgP = Image.open("imatges/Perdre.png")
imgP = imgP.resize((300, 200))
imgP = ImageTk.PhotoImage(imgP)

imgPK = Image.open("imatges/logoPK.png")
imgPK = imgPK.resize((200, 200))
imgPK = ImageTk.PhotoImage(imgPK)

l1 = Label(text="POKEPENJAT", background="white", foreground="Black", width=90, border= 10, anchor="center", font=("Garamond", 10, "bold"))
l1.place(x=0,y=0)

l2 = Label(image=defaultimg)
l2.place(x=50,y=50)

l3 = Label(image=imgPK, bg="#ec363d")
l3.place(x=400,y=150)

eguions = Label(text="", bg="#ec363d")
eguions.place(x=110,y=255)


entrada = Entry(win, validate='key')
entrada.place(x=140,y=289, width=20)
entrada['validatecommand'] = (entrada.register(limit_input), '%P')

entrada.bind("<Return>", comprovar)

marcador_vides = Label(text="Vides: "+str(vides), bg="#ec363d")
marcador_vides.place(x=400,y=50)
marcador_vides.config(font=("Garamond", 10, "bold"))

marcador_lletra = Label(text="Lletres utilitzades: ", bg="#ec363d", wraplength=200)
marcador_lletra.place(x=400,y=90)
marcador_lletra.config(font=("Garamond", 10, "bold"))

marcador_partides = Label(text="Partides jugades: ", bg="#ec363d")
marcador_partides.place(x=400,y=70)
marcador_partides.config(font=("Garamond", 10, "bold"))

#Botons
bcomençar = Button(text="Començar", command=començar)
bcomençar.place(x=70,y=320)
bsortir = Button(text="Sortir", command=win.destroy)
bsortir.place(x=170,y=320)

win.mainloop()