from tkinter import *
from tkinter import messagebox
import time
import random
import threading
import os
import random
import time
from threading import Thread
import threading
from time import sleep
import playsound
from playsound import playsound
from time import time


#Funcion validar primos
def primo (num):
    if isinstance (num, int) and num>0:#se delimita la entrada para que sea un numero entero y mayor a cero
        dos=2
        num=abs(num)
        if num<=1:
            return "No es Primo"
        else:
            return primo_aux(num,dos)
    else:
        return "error"

#funcion auxiliar de primo en la que se determina si el numero es primo
def primo_aux(num,dos):
    modulo=num%dos
    if num==1:
        return "No es primo"
    elif modulo==0:
        return "No es primo"
    elif dos==(num//2):
        return "Es Primo"
    else:
        dos=dos+1
        return primo_aux(num, dos)
    
#funcion que llama a la funcion validar_primos
def llamar_primos():
    try:
        validar_primos()
    except ValueError:
        #cuadro que muestra error si validar_primos es False
        validacion=Label(canvas, text="Error",bg="#F78181",font=("Arial",14),width=15)
        validacion.place(x=800,y=110)

#funcion que valida si el numero es primo o no        
def validar_primos():
    num= int(primos_entrada.get())
    #cuadro que muestra si es primo o no
    validar_primos=Label(canvas,text=primo(num),bg="#F78181",font=("Arial",14),width=15)
    validar_primos.place(x=800,y=110)


#Funcion para calcular el numero fibonacci
def fib(n):
    global a
    a=0
    if isinstance (n,int) and n>-1:
        return fibonacci_aux(n)
    else:
        return "error"
    
#funcion auxiliar que se cumple si el if de la funcion fib
def fibonacci_aux(n):
    global a
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=a+1
        return fibonacci_aux(n-1)+fibonacci_aux(n-2)
    
#funcion que define el tiempo y retorna los calculos a la funcion entrada_fibonacci  
def tiempo(n):
    global a
    tiempo_inicial=time()
    fib2=fib(n)
    tiempo_final=time()
    tiempo_ejecucion=(tiempo_final-tiempo_inicial)
    return "Numero:",fib(n),"Llamadas:",a,"Tiempo:",tiempo_ejecucion

#funcion que valida el dato recibido en la entrada de la intefaz
def llamar_fibonacci():
    try:
        entrada_fibonacci()
    except ValueError:
        #cuadro que muestra "error" si la entrada no es valida
        error1=Label(canvas, text="Error",bg="#F78181",font=("Arial",14),width=25,height=3)
        error1.place(x=745,y=265)
        
#funcion que recibe dato de la interfaz
def entrada_fibonacci():
    n=int(fibonacci_entrada.get())
    #cuadro que muestra los calculos
    validar_tiempo=Label(canvas,text=tiempo(n),bg="#F78181",font=("Arial",14),width=25, wraplength=200, height=3, justify=LEFT)
    validar_tiempo.place(x=745,y=265)
    

#abrir segunda ventana
def abrirventana2():
    ventana.withdraw()
    ventana2=Toplevel()
    ventana2.minsize(800,500)
    ventana2.resizable(width=NO, height=NO)
    ventana2.configure(background="dark turquoise")
    
    #canvas de segunda ventana
    canvas2=Canvas(ventana2, width = 800, height =500)
    canvas2.place(x = -1, y = 0)
    canvas2.configure(background="black")
    
    #cerrar segunda ventana
    def cerrarventana():
        ventana2.destroy()
        ventana.deiconify()
    
    #funcion que define los hilos para que se pueda ejecutar la animacion de cada objeto
    def hilos():
        hilo1=Thread(target = objeto1, args = ())
        hilo1.start()
        hilo2=Thread(target = objeto2, args = ())
        hilo2.start()
        
    #con esta funcion se define el segundo objeto de la animacion
    def objeto1():
        dragon1 = canvas2.create_rectangle(10, 10, 20, 110, fill = "red")#creacion de objeto 2 con su tamaño
        a = 0
        while True:
            if a == 0:
                for i in range(60):
                    canvas2.move(dragon1, 10, 6)
                    ventana2.update()
                    sleep(0.02)
                a = 1
                if a == 1:
                    for i in range(60):
                        canvas2.move(dragon1, -8, -6)
                        ventana2.update()
                        sleep(0.02)
                    a = 0
    #con esta funcion se define el segundo objeto de la animacion
    def objeto2():
        dragon2 = canvas2.create_arc(25, 30, 80, 150, fill = "yellow")#creacion de objeto 2 con su tamaño
        a = 0
        while True:
            if a == 0:
                for i in range(70):
                    canvas2.move(dragon2, 2,5)
                    ventana2.update()
                    sleep(0.01)
                b = 1
                if b == 1:
                    for i in range(70):
                        canvas2.move(dragon2, 0, -5)
                        ventana2.update()
                        sleep(0.1)
                    b = 0
    #Boton de Inicio de animación               
    inicio=Button(ventana2,text="Iniciar",bg="darkorange",command=hilos,font=("Arial",14))
    inicio.place(x=570,y=455)
    #Boton de Cerrar de animación
    boton2= Button(ventana2, text="cerrar animacion",bg="darkorange",font=("Arial",14),command=cerrarventana)
    boton2.place(x=640,y=455)

#funcion de hilos para poder usar funciones en segundo plano mientras se reproduce audio
def hilos():
        hilo3=Thread(target = audio_descriptivo, args = ())#hilo que llama a la funcion que contiene el audio        
        hilo3.start()
        
#funcion que contiene el audio       
def audio_descriptivo():
        playsound("audio.wav")
        
#funcion que activa el audio
def audio():
    global audio1
    audio1=True
    n=Thread(target=audio_descriptivo,args=())
    n.start()

#Crear ventana principal
ventana=Tk()
ventana.title("Tarea")
ventana.minsize(1080,720)
ventana.resizable(width=NO, height=NO)

#Crear Canvas
canvas=Canvas(ventana,width=1080,height=720,bg="#40FF00")
canvas.place(x=-2,y=-2)
canvas.pack()

#Fondo Canvas    
fondo1=PhotoImage(file="Image/fondo.gif")
fondo_magic=Label(canvas, image=fondo1)
fondo_magic.place(x=-1, y=0)

#Etiqueta Ficha
ficha=Label(canvas,text="Ficha de Estudiante:",bg="purple",font=("Arial",14),fg="white",width=16)
ficha.place(x=15,y=20)

#Etiqueta Nombre
nombre=Label(canvas,text="Nombre: Jose David Sánchez Schnitzler",bg="#BDBDBD",font=("Arial",11),width=30)
nombre.place(x=15,y=280)

#Etiqueta Carnet
carnet=Label(canvas,text="Carnet: 2018142388",bg="#BDBDBD",font=("Arial",11),width=15)
carnet.place(x=15,y=305)

#Etiqueta Genero
genero=Label(canvas,text="Genero: Masculino",bg="#BDBDBD",font=("Arial",11),width=14)
genero.place(x=15,y=330)

#Etiqueta Edad
edad=Label(canvas,text="Edad: 19 años",bg="#BDBDBD",font=("Arial",11),width=11)
edad.place(x=15,y=355)

#Etiqueta Dirección
direccion=Label(canvas,text="Dirección: 1.5 km norte de la Basílica de\n los Ángles, hasta Bar Las Vegas Churruca",bg="#BDBDBD",font=("Arial",11),width=32)
direccion.place(x=15,y=415)

#Etiqueta juego
juego=Label(canvas,text="Juego: Magic",bg="#2EFEC8",font=("Arial",14),width=10)
juego.place(x=500,y=20)

#Descripcion del juego
descripcion=Label(canvas,text="Es un juego de cartas de cartas creado\n por Richard Garfield, un profesor de\n de matemáticas de la universidad de \n Pennsylvania",bg="#58FAF4",font=("Arial",11),width=29)
descripcion.place(x=420,y=55)

#Etiqueta Primos
primos=Label(canvas,text="Validar Primos:",bg="#FE2E2E",font=("Arial",14),width=15)
primos.place(x=800,y=20)

#Entrada de Primos
primos_entrada=Entry(canvas,font=("Arial",12),width=19,bg="#F78181")
primos_entrada.place(x=798,y=50)

#Boton primos
primos_boton=Button(canvas,text="Validar",font=("Arial",12),width=10,bg="#FA5858",command=llamar_primos)
primos_boton.place(x=836,y=75)

#Etiqueta Fibonacci
fibonacci=Label(canvas,text="Calcular Fibonacci:",bg="#FE2E2E",font=("Arial",14),width=15)
fibonacci.place(x=800,y=175)

#Entrada de Fibonacci
fibonacci_entrada=Entry(canvas,font=("Arial",12),width=19,bg="#F78181")
fibonacci_entrada.place(x=798,y=205)

#Boton fibonacci
fibonacci_boton=Button(canvas,text="Calcular",font=("Arial",12),width=10,bg="#FA5858",command=llamar_fibonacci)
fibonacci_boton.place(x=836,y=230)

#Imagen de mapa
mapa1=PhotoImage(file="Image/mapa.gif")
mapa=Label(ventana,image=mapa1)
mapa.place(x=20,y=460)

#Imagen de programador
foto=PhotoImage(file="Image/foto.gif")
fotografia=Label(ventana,image=foto)
fotografia.place(x=30,y=70)

#Imagen de juego
magic=PhotoImage(file="Image/juego.gif")
magic_card=Label(ventana,image=magic)
magic_card.place(x=448,y=135)

#Boton animacion
animacion_boton=Button(canvas,text="Animación",font=("Arial",20),width=10,bg="yellow",command=abrirventana2)
animacion_boton.place(x=800,y=600)

#Boton de audio
audio_boton=Button(canvas,text="Audio Descriptivo",font=("Arial",14),width=14,bg="yellow",command=audio)
audio_boton.place(x=475,y=450)

ventana.mainloop()#Final del programa
