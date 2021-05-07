# Código modificado
# David Damián Galán
# Angélica Sofía Ramírez Porras
from turtle import *  # Importa la herramienta turtle
from freegames import vector  # Importa la biblioteca freegames
from math import sqrt  # Importa la funcion sqrt
from math import pi  # Importa la constante pi


def line(start, end):
    """
    Dibuja una línea de acuerdo a dos puntos marcados por dos clicks
    start = punto de inicio
    end = punto de fin
    """
    up()  # Para dejar a dibujar (levantar el lápiz)
    # Mover el lápiz a la coordenada (dupla) que marca el cursor al inicio
    goto(start.x, start.y)
    down()  # Para empezar a dibujar (bajar el lápiz)
    # Mover el lápiz a la coordenada que marca el cursor al final
    goto(end.x, end.y)


def square(start, end):
    """
    Dibuja un cuadrado de acuerdo a dos puntos marcados por dos clicks.
    start = punto de inicio
    end = punto de fin
    """
    up()  # Para dejar a dibujar (levantar el lápiz)
    # Mover el lápiz a la coordenada que marca el cursor al inicio
    goto(start.x, start.y)
    down()  # Para empezar a dibujar (bajar el lápiz)
    begin_fill()  # Para activar la función de rellenar la figura

    for count in range(4):  # Para hacer un loop de 4 veces
        # Para mover el lápiz y formar una línea las veces que indique el loop
        forward(end.x - start.x)
        left(90)  # Hacer girar el lápiz a 90 grados

    end_fill()  # Para rellenar la figura justo después de terminar el loop


def circle(start, end):
    """
    Dibuja un círculo de acuerdo a dos puntos marcados por dos clicks.
    start = punto de inicio
    end = punto de fin
    """
    up()  # Para dejar a dibujar (levantar el lápiz)
    diameter = end.x - start.x  # Define el diámetro con coordenadas
    # Mover el lápiz a la coordenada que marca el cursor al inicio
    goto(start.x, start.y)
    down()  # Para comenzar a dibujar (bajar el lápiz)
    begin_fill()  # Para activar la función de rellenar la figura

    for count in range(360):  # Para hacer un loop de 360 veces
        # Para mover el lápiz y formar una línea las veces que indique el loop
        forward((diameter * pi) / 360)  # traza la circunferencia
        left(1)  # Hacer girar el lápiz a 1 grado

    end_fill()  # Rellena figura


def rectangle(start, end):
    """
    Dibuja un rectángulo de acuerdo a dos puntos marcados por dos clicks.
    start = punto de inicio
    end = punto de fin
    """
    up()  # Para dejar de dibujar (levantar el lápiz)
    goto(start.x, start.y)  # Mover el lápiz a la coordenada start
    down()  # Para comenzar a dibujar (bajar el lápiz)
    begin_fill()  # Para activar la función de rellenar la figura

    for count in range(4):  # Ciclo para las 4 líneas
        # Cuando count es 0 o 2, la longitud es diferencia en x
        # Cuando count es 1 o 3, la longitud es diferencia en y
        if count % 2 == 0:
            forward(end.x - start.x)  # Mueve el lápiz y dibuja la línea
        else:
            forward(end.y - start.y)  # Mueve el lápiz y dibuja la línea
        left(90)  # Hace girar el lápiz 90 grados a la izquierda

    end_fill()  # Terminar de rellenar la figura una vez está completa


def triangle(start, end):
    """
    Dibuja un triángulo de acuerdo a dos puntos marcados por dos clicks.
    start = punto de inicio
    end = punto de fin
    """
    setheading(0)  # Inicializa el angulo como 0
    up()  # Para dejar de dibujar (levantar el lápiz)
    goto(start.x, start.y)  # Mover el lápiz a la coordenada start
    begin_fill()  # Para activar la función de rellenar la figura
    down()  # Para comenzar a dibujar (bajar el lápiz)
    goto(end.x, end.y)  # Mover el lápiz a la coordenada end
    left(135)  # Cambia la orientacion del lapiz 135 grados a la izquierda
    # Calcula la distancia entre los puntos start y end
    dist = sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    forward(dist)  # Mover el lápiz una distancia dist
    goto(start.x, start.y)  # Mover el lápiz a la coordenada start
    end_fill()  # Terminar de rellenar la figura una vez que está completa
    setheading(0)  # Reiniciar el angulo como 0


def tap(x, y):
    """
    Guarda el punto de inicio o dibuja la figura
    x = punto en eje x
    y = punto en eje y
    """
    # Se define una variable con un diccionario que guarda una coordenada
    start = state['start']

    if start is None:  # Opción de si es la primera vez que se dibuja
        state['start'] = vector(x, y)  # Se guarda la primera coordenada
    else:
        shape = state['shape']  # Traza la figura indicada
        # Para terminar de dibujar en el punto donde inició
        end = vector(x, y)
        # Variable para llamar las funciones de las figuras
        shape(start, end)
        state['start'] = None  # Para reiniciar y dibujar algo diferente


def store(key, value):
    """
    Guarda el valor de state.
    key = figura
    value = guarda qué figura se dibuja
    """
    state[key] = value  # Variable que guarda la figura en state


# Guarda las coordenadas (start) y la figura (shape)
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)  # Para las medidas de la ventana/pad de dibujo
onscreenclick(tap)  # Para llamar tap desde los clicks del mouse

listen()  # Interfaz, para recolectar eventos (teclas presionadas)
onkey(undo, 'u')  # La instrucción para deshacer
# A partir de esta línea es para configurar color
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  # Color amarillo añadido por Angie
# A partir de esta línea es para configurar figuras
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Termina el programa
done()
