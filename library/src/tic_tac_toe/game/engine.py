from dataclasses import dataclass
from tic_tac_toe.game.players import Player
from tic_tac_toe.game.render import Rendition
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Board, Mark

@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    rendering: Rendition

    def play(self, starting_mark: Mark = Mark("X")) -> None