
from funcions import *


#Forca depen de la vida
def forca():
      global img 

      img = Image.open("imatges/img"+str(vides)+".png")
      img = img.resize((200, 200))
      img = ImageTk.PhotoImage(img)
      l2.config(image=img)

#Convertir palabra en guions
def guions():
    guions = ""
    for i in range(len(aleatori)):
        guions += "-"
    l3.config(text=guions)


win = Tk()
win.geometry("640x400")
win.configure(bg = 'yellow')
win.title('PokePenjat')

l1 = Label(text="Aplicació PenjAPP", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0,columnspan=2)

defaultimg = Image.open("imatges/img0.png")
defaultimg = defaultimg.resize((200, 200))
defaultimg = ImageTk.PhotoImage(defaultimg)

l2 = Label(image=defaultimg)
l2.grid(column=0,row=1,columnspan=2)

l3 = Label(text="Paraula")
l3.grid(column=0,row=2,columnspan=2)

ent1 = Entry()
ent1.grid(column=0,row=3,columnspan=2)

btn2 = Button(text="Jugar", command=guions)
btn2.grid(column=0,row=4,sticky=E)
btn1 = Button(text="Sortir", command=win.destroy)
btn1.grid(column=1,row=4,sticky=W)


win.mainloop()