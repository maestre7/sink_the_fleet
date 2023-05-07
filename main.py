# Native
import sys
import logging
import logging.config
from pathlib import Path

# Third Parties

# Own
from game.main_process import Main_Process
from utils.utils import clear

class Sink_The_Fleet:

    def __init__(self) -> None:
        """
        """

        # we boot and configure the logging
        logging.config.fileConfig("./log/config/logger.ini", 
                                  defaults={'filename': Path('./log/mylog.log')},
                                  disable_existing_loggers=False)
        self.logger = logging.getLogger('STF')

    def initiation(self) -> None:
        """We collect user and start main process
        """
        try:
            name_player = self.user_register()
            game = Main_Process(name_player)
            clear()
            game.menu()

        except Exception as err:
            self.logger.exception(f"initiation - {err}")
            clear()
            sys.exit("Ocurrio un error, Humano estupido")  

    def user_register(self) -> None:
        """We ask the player for their name or username for the game
        """

        try:
            name_player = input("Introduce un nombre de jugador: ")
            return name_player

        except Exception as err:
            self.logger.exception(f"user_register: {err}")



def main():
    app = Sink_The_Fleet()
    app.initiation()
    return 0

if __name__ == '__main__':
    main()