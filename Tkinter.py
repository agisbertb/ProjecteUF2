#sudo apt-get install python3-tk
from tkinter import *
# sudo apt-get install python3-pil python3-pil.imagetk
from PIL import Image, ImageTk

num=1

def forca():
      global img 
      global num

      img = Image.open("img0.jpg")
      img = img.resize((400, 200))
      img = ImageTk.PhotoImage(img)
      l2.config(image=img)
      num+=1

win = Tk()
win.geometry("640x400")
win.configure(bg = 'yellow')
win.title('PokePenjat')

l1 = Label(text="Aplicació PenjAPP", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0,columnspan=2)

defaultimg = Image.open("img0.jpg")
defaultimg = defaultimg.resize((400, 200))
defaultimg = ImageTk.PhotoImage(defaultimg)

l2 = Label(image=defaultimg)
l2.grid(column=0,row=1,columnspan=2)

ent1 = Entry()
ent1.grid(column=0,row=2,columnspan=2)

btn2 = Button(text="Pinta", command=forca)
btn2.grid(column=0,row=3,sticky=E)
btn1 = Button(text="Sortir", command=win.destroy)
btn1.grid(column=1,row=3,sticky=W)

win.mainloop()