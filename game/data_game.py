# Native
import logging
from time import time, localtime, strftime, sleep

# Own
from game.variables import constants

class Data_Game:

    def __init__(self, name) -> None:
        try: 
            self.logger = logging.getLogger(__name__)
            self.data_game = constants["data_game"]
            self.data_game["player"] = name
            self.data_game["beginning"] = strftime("%Y-%m-%d %H-%M-%S", localtime(time()))
            self.data_game["record"].append({}) # Preparamos un dict para el round
        except Exception as err:
            raise Exception(f"Data_Game.__init__")

    def next_round(self):

        try:
            self.data_game["record"].append({}) # Preparamos un dict para el round
            self.data_game["round"] += 1
        except Exception as err:
            self.logger.exception(f"next_round: {err}")
            raise

    def next_player(self):

        try: 
            if self.data_game["num_player"] == self.data_game["turn"]:
                self.data_game["turn"] = 0
            else:
                self.data_game["turn"] += 1
        except Exception as err:
            self.logger.exception(f"next_player: {err}")
            raise 

    def update_board_shoot(self, board_shoot: list):

        try:
            turn = self.data_game["turn"]
            round = self.data_game["round"]
            self.data_game["record"][round][f"board_shoot{turn}"] = board_shoot

        except Exception as err:
            self.logger.exception(f"update_board_shoot: {err}")
            raise 

    def update_board(self, board: list):

        try:
            turn = self.data_game["turn"]
            round = self.data_game["round"]
            self.data_game["record"][round][f"board{turn}"] = board

        except Exception as err:
            self.logger.exception(f"update_board: {err}")
            raise 

    def update_life(self, life: int):

        try:
            turn = self.data_game["turn"]
            round = self.data_game["round"]
            self.data_game["record"][round][f"board{turn}"] = life

        except Exception as err:
            self.logger.exception(f"update_life: {err}")
            raise 

    def add_fleet_coor(self, fleet_coor: list):

        try:
            turn = self.data_game["turn"]
            self.data_game[f"fleet_coor{turn}"] = fleet_coor
        except Exception as err:
            self.logger.exception(f"add_fleet_coor: {err}")
            raise 


        