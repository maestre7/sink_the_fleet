# Native
import logging

# Third Parties
import numpy as np


logger = logging.getLogger(__name__)

# flota por defecto: (tamaño, cantidad)
fleet_default = {(4,1),(3,2),(2,3),(1,4)}

def deploy_fleet(board: list, fleet: dict = fleet_default) -> list:
    try:
        for ship in fleet:
            control_ship = ship[1] # numero de barcos de este tipo a desplegar
            
            while control_ship > 0: ###
                
                board = ship_check_and_deployment(ship[0], board)
                control_ship -= 1
                

        return board
    ####
    except Exception as err:
        logger.exception(f"deploy_fleet {err}")
        raise

def ship_check_and_deployment(ship_length: int, board: list):
    """We generate deployment coordinates and verify if they are occupied
    """

    try:
        busy = True # Flag para controlar el adecuado despliegue
        while busy:
            deploy_ship = create_ship_random(ship_length, len(board))
            busy = [coor for coor in deploy_ship if board[coor] == "O"]
        
        return place_boat(deploy_ship, board)
    except Exception as err:
        logger.exception(f"place_boat {err}")
        raise

def place_boat(ship_coor: list, board: np.array) -> list:
    """We display the ship on the board according to its coordinates
    """

    try:
        for coor in ship_coor:
            board[coor] = "O"

        return board
    
    except Exception as err:
        logger.exception(f"place_boat {err}")
        raise

def create_ship_random(ship_length: int, board_size: int = 10) -> list:
    """Random deployment of a ship
    """

    try:
        ship_random = []
        ship_random.append(new_position_deploy(board_size))
        row_random = ship_random[0][0] # Fila del primer despliegue
        column_random = ship_random[0][1] # Columna del primer despliegue
        # Orientacion aleatoria
        orient = np.random.choice(["N","S","E","W"])

        while len(ship_random) < ship_length:
            if orient == "W":
                column_random = column_random - 1 
            elif orient == "E":
                column_random = column_random + 1
            elif orient == "N":
                row_random = row_random - 1
            elif orient == "S":
                row_random = row_random + 1

            if row_random not in range(board_size) or column_random not in range(board_size):
                ship_random = []
                ship_random.append(new_position_deploy(board_size))
                row_random = ship_random[0][0] # Fila del primer despliegue
                column_random = ship_random[0][1] # Columna del primer despliegue
            else:
                ship_random.append((row_random,column_random))

        return ship_random
    
    except Exception as err:
        logger.exception(f"generate_boards {err}")
        raise


def new_position_deploy(board_size: int = 10) -> tuple:
    """new initial deployment position"""

    return tuple(np.random.randint(0,board_size, size=2))

def generate_boards(size: int = 10, player: int = 2)-> list:
    """create a number of boards depending on the number of players
    """

    try:
        boards = []
        while len(boards) != player:
            board = create_board(size)
            boards.append(board) # player 0

        return boards
    
    except Exception as err:
        logger.exception(f"generate_boards {err}")
        raise


def create_board(size: int =10) -> np.array:
    """Creates a square board, with the given size
    """

    return np.full((size, size), " ")


def load_menu() -> None:
    """show main menu 
    """

    print("*" * 10)
    print(" Hundir la flota ")
    print(" Selecciones una de las siguientes opciones: ")
    print(" 1. Jugar una partida contra la IA")
    print(" 0. Para salir ")
    print(" Recuerda que para salir puedes usa CTRL + C")
    print("*" * 10, end="\n \n")
  