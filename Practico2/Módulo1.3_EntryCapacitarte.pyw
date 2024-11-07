from tkinter import *
raiz=Tk()

miFrame=Frame(raiz, width = 1200, height = 600)
miFrame.pack()
nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0,column=1)
contraseñaLabel=Label (miFrame, text="Contraseña")
contraseñaLabel.grid(row=1,column=1)

cuadroTexto = Entry(miFrame) #Cuadro contenedor
cuadroTexto.grid(row=1,column=2)#Posición
cuadroTexto1= Entry(miFrame) #Cuadro contenedor
cuadroTexto1.grid(row=0,column=2)#Posición

raiz.mainloop()
