from turtle import *# Importa la herramienta turtle
from freegames import vector # Importa la biblioteca freegames
from math import pi
def line(start, end):# Función para dibujar una línea
    "Draw line from start to end."# Comentario de función que explica lo que hace 
    up()# Para dejar a dibujar (levantar el lápiz)
    goto(start.x, start.y)# Mover el lápiz a la coordenada (dupla) que marca el cursor al inicio  
    down()# Para empezar a dibujar (bajar el lápiz)
    goto(end.x, end.y) # Mover el lápiz a la coordenada que marca el cursor al final 

def square(start, end):# Función de cuadrado
    "Draw square from start to end."# Explicación de la función (?)
    up()# Para dejar a dibujar (levantar el lápiz)
    goto(start.x, start.y)# Mover el lápiz a la coordenada que marca el cursor al inicio  
    down()# Para empezar a dibujar (bajar el lápiz)
    begin_fill() # Para activar la función de rellenar la figura 

    for count in range(4):# Para hacer un loop de 4 veces 
        forward(end.x - start.x)# Para mover el lápiz y formar una línea las veces que indique el loop 
        left(90)# Hacer girar el lápiz a 90 grados

    end_fill()#Para rellenar la figura justo después de terminar el loop 

def circle(start, end):# Función del círculo 
    "Draw circle from start to end."
    up()# Para dejar a dibujar (levantar el lápiz)
    diameter = end.x - start.x # Define el diámetro con coordenadas
    goto(start.x,start.y)# Mover el lápiz a la coordenada que marca el cursor al inicio
    down()
    begin_fill()
    for count in range(360):# Para hacer un loop de 360 veces 
        forward((diameter * pi) / 360)# Para mover el lápiz y formar una línea las veces que indique el loop 
        left(1)# Hacer girar el lápiz a 1 grado
    end_fill()# Rellena figura 
      
def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):# Función para empezar a dibujar desde una coordenada x,y 
    "Store starting point or draw shape."# Explicación de la función
    start = state['start']# Se define una variable con un diccionario que guarda una coordenada 


    if start is None:# Opción de si es la primera vez que se dibuja
        state['start'] = vector(x, y)# Se guarda la primera coordenada
    else:
        shape = state['shape']# Traza la figura indicada 
        end = vector(x, y)# Para terminar de dibujar en el punto donde inició 
        shape(start, end)# variable para llamar las funciones de las figuras
        state['start'] = None # Para reiniciar y dibujar algo diferente

def store(key, value):#Función donde se guarda la figura que se va a dibujar  
    "Store value in state at key."
    state[key] = value # Varaible que guarda la figura en state

state = {'start': None, 'shape': line}# Guarda las coordenadas (start) y la figura (shape)
setup(420, 420, 370, 0)# Para las medidas de la ventana/pad de dibujo 
onscreenclick(tap) # Para llamar tap desde los clicks del mouse
listen()# Interfaz 
onkey(undo, 'u') # La instrucción para deshacer 
onkey(lambda: color('black'), 'K')# A partir de esta línea es para configurar color y figuras 
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'),'Y') # color amarillo añadido por Angie
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()