# Native
import logging

# Own
from game.combat_process_functions import shoot_random


class Combat_Process:

    def __init__(self, data_game: dict) -> None:
        self.logger = logging.getLogger(__name__)
        self.data_game = data_game
        self.win = False


    def start_combat(self):


        try:
            while not self.win:
                board_target, board_shoot = self.data_game.recover_board_shoot()

                if self.data_game.data_game["turn"] == 1:
                    board_ship = self.data_game.recover_board_ship()
                    print("Tu situacion es la siguiente:")
                    print(board_ship)
                    print("La leyenda es:")
                    print("' ' es agua")
                    print("'-' es agua bombardeada")
                    print("'O' es barco")
                    print("'X' es barco bombardeada")
                    print("Tu cuadrante de disparos es el siguiente:")
                    print(board_shoot)
                    row_shoot = int(input("Introduce una fila para disparar: "))
                    column_shoot = int(input("Introduce una columna para disparar: "))
                else:
                    row_shoot, column_shoot = shoot_random()

                shoot = self.check_shoot((row_shoot, column_shoot), board_target, board_shoot)

                if not shoot and not self.win:
                    if self.data_game.data_game["num_player"] == self.data_game.data_game["turn"]:
                        self.data_game.next_player()
                        self.data_game.next_round()
                    else:
                        self.data_game.next_player()

        except Exception as err:
            self.logger.exception(f"start_combat: {err}")
            raise


    def check_shoot(self, coor: tuple, board_target: list, board_shoot: list) -> bool:

        try:

            shoot = False
            print("coor:", coor)
            if board_target[coor] == "O":
                board_target[coor] = "X"
                board_shoot[coor] = "X"

                print("Tocado")
                shoot = True
            else:
                board_target[coor] = "-"
                board_shoot[coor] = "-"
                print("Agua")

            self.data_game.update_board_shoot(board_shoot)
            self.data_game.update_board(board_target)

            return shoot
        
        except Exception as err:
            self.logger.exception(f"check_shoot: {err}")
            raise

    def check_life(self,board_target: list,):

        try:
            # Calculamos el numero de vidas = al numero de slots de ocupados por barcos
            life = sum([sum([1 for c in coor if c == "O"]) for coor in board_target])
            self.data_game.update_life(life)
            self.win = True if life == 0 else False

        except Exception as err:
            self.logger.exception(f"check_life: {err}")
            raise
