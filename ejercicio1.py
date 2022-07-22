# se le importa la libreria tkinter con tods sus funciones 
from tkinter import *

#----------------------- 
#---ventana principal---
#-----------------------

# Se declara una variable que llamamos ventana_principal y que te adquiere las caracteristicas de un objeto Tk()

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Jenny Romero")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x300")

#icono de ventana principal 
#ventana.principal

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="RosyBrown1")

# agregamos un widget a la ventana principal
Letrero= Label(text="\n\nSistemas, la mejor!!\n\n" , bg="ivory3")
Letrero.pack()

# agregamos un widget a la ventana principal
Letrero2= Label(text="\n\nJenny Romero\n\n" , bg="ivory3")
Letrero2.pack()

# agregamos un widget a la ventana principal
Letrero3= Label(text="\n\nColegio san jose de Guanenta\n\n" , bg="ivory3")
Letrero3.pack()

#se ejecuta el metodo mainloop de la clase Tk a traves de la istancia ventana principal. Este metedo despliega una ventana simple en pantalla y queda ala espera de lo que el usuario haga.por ejemplo,click en el boton escribir en caja de texto, etc.cada accion del usuario se conoce como un evento. El metodo mainloop es bucle infinitivo

ventana_principal.mainloop()