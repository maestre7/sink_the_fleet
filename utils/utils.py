# Native
import os

def clear() -> None:
    """Clear console
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")