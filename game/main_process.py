
# Native
import logging
from time import time, localtime, strftime, sleep

# Third Parties
import numpy as np

# Own
from game.main_process_functions import load_menu, clear, generate_boards, deploy_fleet



class Main_Process:

    def __init__(self, name_player: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.name_player = name_player
        

    def menu(self) -> None:
        """We load the menu with the different options and redirect
        """

        try:
            load_menu() # Cargamos el menu con las distitas opciones

            option = int(input("Elija el numero de la opcion"))

            if option == 1:
                self.game_against_ai()

        except ValueError:
            ### preparar una unica str o cargar desde un fichero multi idioma
            clear()
            print("!" * 10) 
            print(" Solo se admiten numeros")
            print("!" * 10)
            print("")
            sleep(3000)
            clear()
            self.menu()

        except Exception as err:
            self.logger.exception(f"menu {err}")
            raise


    def game_against_ai(self) -> None:
        """
        """

        try: ### datos basicos de partida
            round_zero = np.array()
            data_game = {"style": 0, # 1 playervsplayer, 0 playervsia
                         "round": 0,
                         "turn": 1, # 0 ia, 1 player one , 2 player two
                         "player": self.name,
                         "beginning": strftime("%Y-%m-%d %H-%M-%S", localtime(time())),
                         "record": np.array()}

            boards = generate_boards() # default size 10 and player 2
            for board in boards:
                # Por cada jugador desplegamos las flotas
                round_zero.append(deploy_fleet(board)) 

        except Exception as err:
            self.logger.exception(f"game_against_ai {err}")
            raise