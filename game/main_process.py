
# Native
import logging

# Own
from game.main_process_functions import load_menu



class Main_Process:

    def __init__(self, name_player: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.name_player = name_player
        


    def menu(self):
        try:
            load_menu() # Cargamos el menu con las distitas opciones

            option = int(input("Elija el numero de la opcion"))
            
        except ValueError:
            print(" Solo se admiten numeros ")
            self.menu()

        except Exception as err:
            self.logger.exception(f"menu {err}")


