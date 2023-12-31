import abc
import time
from tic_tac_toe.logic.models import Mark, GameState, Move
from tic_tac_toe.logic.exceptions import InvalidMove


class Player(metaclass=abs.ABCMeta):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("Possible Moves are no longer available")
        else:
            raise InvalidMove("It's the turn of the other player")

    @abc.abstractclassmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state"""


class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.3) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)
