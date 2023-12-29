from __future__ import annotations
import enum
import re
from dataclasses import dataclass
from functools import cached_property
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.validate import validate_board, validate_game_state

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",)


class Mark(str, enum.Enum):
    """
    Python will store the players and the marks they use using
    the Mark class. it holds the valid cross and circle symbols.
    """
    CROSS = "X"
    CIRCLE = "O"

    @property
    def toggle(self) -> "Mark":
        """function will switch to the other player given current player."""
        if self is Mark.CIRCLE:
            return Mark.CROSS
        else:
            return Mark.CIRCLE


@dataclass(frozen=True)
class Board:
    """
    Python will internally save the board state in a string.
    The following class methods allow for characterization of the
    Board and the decorators allow for their storing in cache.
    Storing in cache works because our board is immutable, thus all
    class attributes can be calculated once and stored in cache memory.
    """
    cells: str = " " * 9

    def __post_init__(self) -> None:
        validate_board(self)

    @cached_property
    def cross_count(self) -> int:
        """store number of X in cache"""
        return self.cells.count("X")

    @cached_property
    def circle_count(self) -> int:
        """store number of O in cache"""
        return self.cells.count("O")

    @cached_property
    def space_count(self) -> int:
        """store number of empty/available spaces in cache"""
        return self.cells.count(" ")


@dataclass(frozen=True)
class Move:
    """
    Store all the information for a move in this class.
    Relevant information will include the mark that needs to be placed,
    and the location of where it will placed in the string by index
    """
    mark: Mark
    cell_index: int
    prev_state: "GameState"
    next_state: "GameState"


@dataclass(frozen=True)
class GameState:
    """
    Stores the current state of the game. There are only 5 possible states:
    1. The game has not yet started
    2. The game is currently underplay and has not yet ended
    3. The game has ended in a tie
    4. The game has ended in a win for cross (X)
    5. The game has ended in a win for circles (O)
    """
    board: Board
    first_player: Mark = Mark("X")  # by convention X goes first

    def __post_init__(self) -> None:
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        """
        The function determines whose turn it is currently.
        Based on the logic that if there are equal number of
        X ans O then it must be the turn of the player that started
        the game initially. Otherwise it is the other players turn.
        """
        if self.board.cross_count == self.board.circle_count:
            return self.first_player
        else:
            return self.first_player.toggle

    @cached_property
    def game_has_started(self) -> bool:
        """If the game has started then the number of empty spaces will be less than 9."""
        return True if self.board.space_count != 9 else False

    @cached_property
    def game_is_over(self) -> bool:
        """a game ends in tie when all spaces are used up or when there is a winner."""
        return True if self.winner is not None or self.tie else False

    @cached_property
    def tie(self) -> bool:
        """Game ends when there is a tie and all spaces are used up."""
        if self.winner is None and self.board.space_count == 0:
            return True
        else:
            return False

    @cached_property
    def winner(self) -> Mark | None:
        """Find the winner and return which one was it. otherwise show None if tied"""
        for item in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(item.replace("?", mark), self.board.cells):
                    return mark
        return None

    @cached_property
    def winning_combo(self) -> list[int]:
        """return the combination of cells that gained victory. Use this function later
        to help in visualization of the pattern."""
        for item in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(item.replace("?", mark), self.board.cells):
                    return [match.start() for match in re.finditer(r"\?", item)]
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        """The re module has an iteration maker that simplifies the searching process"""
        moves = []
        if not self.game_is_over:
            for match in re.finditer(r"\s", self.board.cells):
                moves.append(self.make_move(match.start()))
        return moves

    def make_move(self, idx: int) -> Move:
        """This is the move generator function"""
        if self.board.cells[idx] != " ":
            # Check if it is an empty slot, otherwise throw error
            raise InvalidMove("Cell is not available.")
        return Move(
            mark=self.current_mark,
            cell_index=idx,
            prev_state=self,
            next_state=GameState(
                Board(
                    self.board.cells[:idx]
                    + self.current_mark
                    + self.board.cells[idx+1:]
                ),
                self.first_player,
            ),
        )
