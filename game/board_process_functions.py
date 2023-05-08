# Native
import logging

# Third Parties
import numpy as np


logger = logging.getLogger(__name__)


def create_board(size: int =10) -> np.array:
    """Creates a square board, with the given size
    """

    try:
        return np.full((size, size), " ")

    except Exception as err:
        logger.exception(f"create_board: {err}")
        raise

def ship_check_and_deployment(ship_length: int, board: list):
    """We generate deployment coordinates and verify if they are occupied
    """

    try:
        busy = True # Flag para controlar el adecuado despliegue
        while busy:
            deploy_ship = create_ship_random(ship_length, len(board))
            busy = [coor for coor in deploy_ship if board[coor] == "O"]

        board = place_boat(deploy_ship, board)
        return (board, deploy_ship)
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
