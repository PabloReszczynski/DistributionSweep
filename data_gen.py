#!/usr/bin/python3

from numpy.random import normal, uniform, randint
import sys

def generate(position, separation, direction, size):
    """
    Genera, a partir de listas randomizadas de puntos, separaciones y
    direcciones una lista de lineas.

    Parameters:
    ==========
        position: list
            Lista de 2-tuplas conteniendo puntos (x, y) randomizados.
        separation: list
            Lista de floats que describe la separacion de 2 puntos de forma
            randomizada.
        direction: list
            Lista que contiene 1s o 0s. Define que la linea i es horizontal o
            vertical.
        size: int
            Numero de lineas

    Returns:
    =======
        data: list
            Lista de 4-tuplas conteniendo 2 puntos.
    """
    (x, y) = position
    data = []

    for i in range(size):
        x1 = x[i]
        y1 = y[i]
        if direction[i] == 1: # horizontal
            x2 = x1 + separation[i]
            y2 = y1
        else:                 # vertical
            x2 = x1
            y2 = y1 + separation[i]

        data.append((x1, y1, x2, y2))

    return data

def generate_normal(size):
    """
    Genera lineas con una distribucion normal.

    Parameters:
    ==========
        size: int
            Numero de lineas

    Returns:
    =======
        data: list
            Lista de 4-tuplas conteniendo 2 puntos.
    """
    position = (normal(scale=5.0, size=size),
                normal(scale=5.0, size=size))
    separation = normal(scale=2.0, size=size)
    direction = randint(low=0, high=2, size=size)
    return generate(position, separation, direction, size)

def generate_uniform(size):
    """
    Genera lineas con distribucion uniforme

    Parameters:
    ==========
        size: int
            Numero de lineas

    Returns:
    =======
        data: list
            Lista de 4-tuplas conteniendo 2 puntos.
    """
    position = (random.uniform(size=size), random.uniform(size=size))
    separation = random.uniform(size=size)
    direction = random.randint(low=0, high=2, size=size)
    return generate(position, separation, direction, size)

def write_data(data):
    """
    Escribe los resultados de la generacion a un archivo con formato csv,
    separado por comas.
    """
    with open('data.csv', 'w') as csv:
        csv.write('\n'.join('%s,%s,%s,%s' % x for x in data))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('ERROR: No argument provided')
        sys.exit(1)
    num_lines = int(sys.argv[1])
    print('Generating Normal Distribution for %s lines' % num_lines)
    data = generate_normal(num_lines)
    write_data(data)
    print("Done")
