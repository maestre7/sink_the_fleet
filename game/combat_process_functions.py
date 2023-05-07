# Native
import logging

# Third Parties
import numpy as np

logger = logging.getLogger(__name__)

def shoot_random(board_size: int = 10) -> tuple:
    """shoot_random"""

    return tuple(np.random.randint(0,board_size, size=2))

def collect_coordinates():

    try:
        row_shoot = int(input("Introduce una fila para disparar: "))
        column_shoot = int(input("Introduce una columna para disparar: "))
    except ValueError:
        print("!" * 10) 
        print(" Solo se admiten numeros")
        print("!" * 10)
        collect_coordinates()
    else:   
        print(row_shoot, column_shoot) 
        return (row_shoot, column_shoot)