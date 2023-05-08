# Native
import logging

# Third Parties
import numpy as np

# Own
from game.variables import constants
from game.board_process_functions import create_board, ship_check_and_deployment



class Board:

    def __init__(self) -> None:
        """Load a blank board for future shots and initialize the board list
        """

        try:
            self.logger = logging.getLogger(__name__)
            self.board_clear = create_board()
            self.fleet_default = constants["fleet_default"]
            self.boards = []

        except Exception:
            raise Exception(f"Boards.__init__")


    def generate_boards(self, size: int = 10, player: int = 2) -> np.array:
        """We generate a dashboard that we return, 
        and that we add to the dashboard registry.
        """

        try:
            # Generamos tableros
            while len(self.boards) != player:
                board = create_board(size) # default size 10 and player 2
                self.boards.append(board)

            return self.boards

        except Exception as err:
            self.logger.exception(f"generate_boards: {err}")
            raise

    def deploy_fleet(self, board: list, fleet: list = None) -> list:
        """We deploy a number of ships on the board
        """

        try:
            fleet = self.fleet_default if fleet == None else fleet
            fleet_coor = []
            for ship in fleet:
                control_ship = ship[1] # numero de barcos de este tipo a desplegar
                
                while control_ship > 0: ###
                    board, deploy_ship = ship_check_and_deployment(ship[0], board)
                    fleet_coor.append(deploy_ship)
                    control_ship -= 1
      
            return (board, fleet_coor)

        except Exception as err:
            self.logger.exception(f"deploy_fleet {err}")
            raise
