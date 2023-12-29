from tic_tac_toe.logic.validate import validate_players
from tic_tac_toe.logic.models import GameState, Board, Mark
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.game.renderers import Rendition
from tic_tac_toe.game.players import Player
from dataclasses import dataclass
from typing import Callable, TypeAlias
ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    player1: Player
    player2: Player
    rendering: Rendition
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_players(self.player1, self.player2)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        game_state = GameState(Board(), starting_mark)
        while True:
            self.rendering.render(game_state)
            if game_state.game_is_over:
                break
            player = self.get_curr_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_curr_player(self, game_state: GameState) -> Player:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
