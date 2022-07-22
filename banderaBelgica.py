# se le importa la libreria tkinter con tods sus funciones 
from tkinter import *

#----------------------- 
#---ventana principal---
#-----------------------

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Belgica")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

#color de fondo de la ventana principal
ventana_principal.config(bg="grey1")

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="grey1", width=300, height=800)
frame_entrada.place(x=10,y=10)

#-----------------
# frame amarillo
#-----------------
frame_amarillo = Frame(ventana_principal )
frame_amarillo.config (bg="yellow", width=300, height=800)
frame_amarillo.place(x=280,y=10)

#-----------------
# frame rojo
#-----------------
frame_rojo = Frame(ventana_principal )
frame_rojo.config (bg="red", width=400, height=800)
frame_rojo.place(x=500,y=10)

ventana_principal.mainloop()