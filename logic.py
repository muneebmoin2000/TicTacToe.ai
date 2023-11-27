from numpy import random
from game_state import Board

class Rules(Board):
    """Abstract away the class by making a different class and file for the rules of the"""
    def __init__(self):
        Board.__init__(self)
        self.players = ["X","O"]
        self.curr_player = random.choice(self.players)
        self.winner = None
        self.end_states = ["X Wins", "O Wins", "Tied Game","Please Continue Game","Please Start the Game"]
        self.used_spots = 0

    def check_winner(self):
        """If there are spots still available,
         winner could still be determined based on the moves """
        
        for i in range(3):
            #horizontal
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                self.winner = self.board[i][0]
            #vertical
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                self.winner = self.board[0][i]
        #diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
        
        return self.winner
        
    def ending_state(self):
        #check the final end-state of the game and return it
        #Its possible that the game never started in which is also an edge case
        if self.used_spots == 0:
            return self.end_states[4]
        if self.check_winner() is None and self.used_spots < 9:
            return self.end_states[3]
        if self.check_winner() is None and self.used_spots == 9:
            return self.end_states[2]
        if self.check_winner() == self.players[1]:
            return self.end_states[1]
        if self.check_winner() == self.players[0]:
            return self.end_states[0]