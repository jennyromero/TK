# se le importa la libreria tkinter con tods sus funciones 
from tkinter import *

#----------------------- 
#---ventana principal---
#-----------------------

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Costa Rica")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

#color de fondo de la ventana principal
ventana_principal.config(bg="grey1")

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="blue", width=800, height=70)
frame_entrada.place(x=10,y=10)


#-----------------
# frame blanco
#-----------------
frame_blanco = Frame(ventana_principal )
frame_blanco.config (bg="grey86", width=800, height=130)
frame_blanco.place(x=10,y=70)


#-----------------
# frame rojo
#-----------------
frame_rojo = Frame(ventana_principal )
frame_rojo.config (bg="red", width=800, height=200)
frame_rojo.place(x=10,y=160)

#-----------------
# frame 2
#-----------------
frame_2 = Frame(ventana_principal )
frame_2.config (bg="grey86", width=800, height=90)
frame_2.place(x=10,y=330)

#-----------------
# frame resultado
#-----------------
frame_azul = Frame(ventana_principal )
frame_azul.config (bg="blue", width=800, height=90)
frame_azul.place(x=10,y=400)

ventana_principal.mainloop()