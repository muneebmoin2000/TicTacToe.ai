from game_state import Board
from logic import Rules

b = Board()
r = Rules()
b.visualize(r.check_winner())