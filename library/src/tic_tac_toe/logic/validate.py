from __future__ import annotations
from typing import TYPE_CHECKING
import re
from tic_tac_toe.logic.exceptions import InvalidGameState

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import Board, GameState, Mark


def validate_board(board: Board) -> None:
    """
    After initialization of the Board, must make sure that the initialization
    was that of a 9 character string that only holds valid entries: X, O or space.
    """
    if not re.match(r"^[\sXO]{9}$", board.cells):
        # Use for loop to do a linear search of the string characters for verification.
        raise ValueError(
            "Incorrect Initialization: Must be 9 units. Grid must be holding X, O or space only")


def validate_game_state(game_state: GameState) -> None:
    validate_mark_count(game_state.board)
    validate_starting_mark(game_state.board, game_state.first_player)
    validate_winner(game_state.board, game_state.first_player,
                    game_state.winner)


def validate_mark_count(board: Board) -> None:
    if abs(board.cross_count - board.circle_count) > 1:
        raise InvalidGameState("Incorrect count of X's and O's")


def validate_starting_mark(board: Board, starting_mark: Mark) -> None:
    if board.cross_count > board.circle_count and starting_mark != "X":
        raise InvalidGameState("Incorrect starting mark")
    elif board.circle_count > board.cross_count and starting_mark != "O":
        raise InvalidGameState("Incorrect starting mark")


def validate_winner(board: Board, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == "X":
        if starting_mark == "X":
            if board.cross_count <= board.circle_count:
                raise InvalidGameState("Incorrect count of crosses")
        else:
            if board.cross_count != board.circle_count:
                raise InvalidGameState("Incorrect count of crosses")
    elif winner == "O":
        if starting_mark == "O":
            if board.circle_count <= board.cross_count:
                raise InvalidGameState("incorrect number of circles")
        else:
            if board.circle_count != board.cross_count:
                raise InvalidGameState("Incorrect number of circles")
