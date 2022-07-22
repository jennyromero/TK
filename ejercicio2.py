# se le importa la libreria tkinter con tods sus funciones 
from os import pread
from tkinter import *
from tkinter import messagebox

#-------------------
#funciones de la app
#-------------------

def sumar():
    messagebox.showinfo("Suma 1.0", " Hizo click en el boton sumar...")
    c= int(a.get()) + int(b.get())
    t_resultado.insert(INSERT, " La suma de " + a.get() +  " + " + b.get() + " casi siempre es " + str(c)+"\n")

def borrar ():
    messagebox.showinfo("Suma 1.0", " Los datos seran borrados...")
    a.set("")
    b.set("")
    t_resultado.delete("1.0","end")
    
def salir():
        messagebox.showinfo("Suma 1.0", "La app se cerrara...") 
        ventana_principal.destroy()

#----------------------- 
#---ventana principal---
#-----------------------

# Se declara una variable que llamamos ventana_principal y que te adquiere las caracteristicas de un objeto Tk()

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Jenny Romero")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

#icono de ventana principal 
#ventana.principal

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="grey1")

#---------------------
# variables globales
#---------------------

a= StringVar()
b= StringVar()
C= StringVar()

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="aquamarine", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo= Label(frame_entrada, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue" , font=("Arial", 16))
titulo.place(x=240, y=10)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text ="Especialidad en sistemas")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=240, y=40)

#Etiqueta para el subtitulo2 de la app
subtitulo2 =Label(frame_entrada, text="SUMA DE DOS ENTEROS")
subtitulo.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240, y=70)

# imagen - logo de la app 
logo = PhotoImage(file="escudo.png")
etiq_logo = Label (frame_entrada,image=logo)
etiq_logo.place(x=10, y=10)

#Etiqueta para valor a
etiq_a = Label(frame_entrada, text="a = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=390, y=120)

#Entry para valor a
entry_a = Entry(frame_entrada,width=4, textvariable=a)
entry_a .config(font=("Arial", 20), justify=CENTER)
entry_a .focus_set()
entry_a.place(x=487, y=120)

#Etiqueta para valor b
etiq_b = Label(frame_entrada, text="a = ")
etiq_b .config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=585, y=120)

#Entry para valor b
entry_b = Entry(frame_entrada)
entry_b .config(font=("Arial", 20),width=4, textvariable=b)
entry_b .config(font=("Arial", 20))
entry_b.place(x=682, y=120)

#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="azure3", width=780, height=120)
frame_operaciones.place(x=10,y=260)

#boton para sumar los numeros - texto
bt_sum =PhotoImage(file="sumar1.png")
# bt_sumar = Button(frame_operaciones, text="Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum,width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

#boton para borrar entradas y resultado 
bt_bor =PhotoImage(file="eliminar.png")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor,width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

#boton para salir - cerrar la app
bt_sal =PhotoImage(file="salir.png")
# bt_salir = Button(frame_operaciones, text="salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal,width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)

#-----------------
# frame resultados
#-----------------

frame_resultados= Frame(ventana_principal )
frame_resultados.config (bg="seashell3", width=780, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para resultado
t_resultado=Text(frame_resultados, width=96, height=3)
t_resultado.config(bg="SkyBlue3", fg="white", font=("Arial", 20))
t_resultado.pack()

#se ejecuta el metodo mainloop de la clase Tk a traves de la istancia ventana principal. Este metedo despliega una ventana simple en pantalla y queda ala espera de lo que el usuario haga.por ejemplo,click en el boton escribir en caja de texto, etc.cada accion del usuario se conoce como un evento. El metodo mainloop es bucle infinitivo

ventana_principal.mainloop()