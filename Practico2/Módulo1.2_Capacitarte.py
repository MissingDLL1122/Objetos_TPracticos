from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 1000, height =980 )
miFrame.pack()

miLabel = Label(miFrame, text = "Hola Mundo", fg="gray", font=("Comic Sans MS",18)).place(x=195,y=200)
miImg = PhotoImage(file="C:\\Objetos-TPracticos\\Practico2\\Seba.png.png")  #pide usar barras dobles en la ruta de dirección.. 
Label(miFrame, image=miImg).place(x = 150, y = 300)


raiz.mainloop()
