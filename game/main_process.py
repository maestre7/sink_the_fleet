
# Native
import logging
from copy import deepcopy
from time import sleep

# Third Parties
#import numpy as np

# Own
from game.main_process_functions import load_menu
from game.board_process import Board
from game.combat_process import Combat_Process
from game.data_game import Data_Game
from utils.utils import clear



class Main_Process:

    def __init__(self, name_player: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.name_player = name_player


    def menu(self) -> None:
        """We load the menu with the different options and redirect
        """

        try:
            try:
                load_menu() # Cargamos el menu con las distitas opciones

                option = int(input("Elija el numero de la opcion "))

            except ValueError:
                ### preparar una unica str o cargar desde un fichero multi idioma
                clear()
                print("!" * 10)
                print(" Solo se admiten numeros")
                print("!" * 10)
                print("")
                sleep(3)
                clear()
                self.menu()

            else:
                if option == 1:
                    self.game_against_ai()

        except Exception as err:
            self.logger.exception(f"menu: {err}")
            raise
        
        
    def game_against_ai(self) -> None:
        """
        """

        try: ### datos basicos de partida
            data_game = Data_Game(self.name_player)
            
            # Generamos tableros
            board_game = Board()
            boards = board_game.generate_boards() # default size 10 and player 2
            
            for board in boards:

                # Por cada jugador desplegamos las flotas
                # Recuperamos las coordenadas de los barcos.
                deploy_board, fleet_coor = board_game.deploy_fleet(board)

                # Calculamos el numero de vidas = al numero de slots de ocupados por barcos
                life = sum([sum([1 for c in coor if c == "O"]) for coor in deploy_board])

                data_game.add_fleet_coor(fleet_coor)
                data_game.update_board_shoot(deepcopy(board_game.board_clear))
                data_game.update_board(deploy_board)
                data_game.update_life(life)
                data_game.next_player()

            combat = Combat_Process(data_game)
            combat.start_combat()

            print("Vete a casa y dejame en paz")
            

        except Exception as err:
            self.logger.exception(f"game_against_ai: {err}")
            raise 