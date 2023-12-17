import re
from tic_tac_toe.logic.models import Board


def validate_board(board: Board) -> None:
    if not re.match(r"^[sXO]{9}$", board.cells):
        raise ValueError("Must be only 9 units using X, O, or space")
