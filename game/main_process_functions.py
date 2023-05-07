# Native
import logging

# Third Parties
import numpy as np

# Own
#from game.variables import constants

logger = logging.getLogger(__name__)


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
  