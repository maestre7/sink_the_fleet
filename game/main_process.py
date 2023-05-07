
# Native
import logging
from time import time, localtime, strftime, sleep

# Third Parties
import numpy as np

# Own
from game.main_process_functions import load_menu, generate_boards, deploy_fleet
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
                #clear()
                print("!" * 10) 
                print(" Solo se admiten numeros")
                print("!" * 10)
                print("")
                sleep(3)
                #clear()
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
            data_game = {"style": 0, # 1 playervsplayer, 0 playervsia
                         "round": 0,
                         "turn": 1, # 0 ia, 1 player one , 2 player two
                         "player": self.name_player,
                         "beginning": strftime("%Y-%m-%d %H-%M-%S", localtime(time())),
                         "record": []}
            # Generamos tableros
            boards = generate_boards() # default size 10 and player 2
            data_game["record"].append({}) # Preparamos un dict para el round

            for index, board in enumerate(boards):
                # Por cada jugador desplegamos las flotas
                deploy_board = deploy_fleet(board)
                # Calculamos el numero de vidas = al numero de slots de ocupados por barcos
                life = sum([sum([1 for c in coor if c == "O"]) for coor in deploy_board])
                data_game["record"][0][f"board{index}"] = deploy_board
                data_game["record"][0][f"life_player{index}"] = life

            print(data_game["record"][0])
            

        except Exception as err:
            self.logger.exception(f"game_against_ai: {err}")
            raise 