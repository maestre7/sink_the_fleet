# Native
import logging

# Third Parties
import numpy as np

logger = logging.getLogger(__name__)

def shoot_random(board_size: int = 10) -> tuple:
    """shoot_random"""

    return tuple(np.random.randint(0,board_size, size=2))