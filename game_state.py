from numpy import array, random

class Board():
    """Board class made to store the current game state of the tictactoe board; 
    search and evaluation classes will be stored in seperate files"""    
    
    def __init__(self):
        """The constructor will initialize the board with empty values
        The entire game state of the board is being stored as a python list."""

        self.board = array([
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ])
        self.teams = ["X","O"]
        self.curr_player = random.choice(["Computer","Myself"])
        self.winner = None
        self.end_states = ["X Wins", "O Wins", "Tied Game","Please Continue Game","Please Start the Game"]
        self.used_spots = 0
        self.available_moves = []


    def visualize(self,boards):
        """This function is useful for displaying the game onto the console for now;
        In future implementations, this console centric display will be replaced with a GUI"""

        print()
        print(f" {boards[0][0]} | {boards[0][1]} | {boards[0][2]} ")
        print("---+---+---")
        print(f" {boards[1][0]} | {boards[1][1]} | {boards[1][2]} ")
        print("---+---+---")
        print(f" {boards[2][0]} | {boards[2][1]} | {boards[2][2]} ")
        print()

    def check_state(self):
        """If there are spots still available,
         winner could still be determined based on the moves """
        
        if self.used_spots == 0:
            return self.end_states[4]
        
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
        
        if self.winner is None and self.used_spots < 9:
            return self.end_states[3]
        if self.winner is None and self.used_spots == 9:
            return self.end_states[2]
        if self.winner == self.teams[1]:
            return self.end_states[1]
        if self.winner == self.teams[0]:
            return self.end_states[0]
        
    # def ending_state(self):
    #     """check the final end-state of the game and return it
    #     Its possible that the game never started in which is also an edge case"""
    def toggle_player(self):
        if self.curr_player == self.teams[0]:
            self.curr_player = self.teams[1]
        else:
            self.curr_player = self.teams[0]
    
    def move_finder(self):

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.available_moves.append([i,j])
                else:
                    continue

    def play_game(self):
        [i,j] = (random.choice([0,1,2]),random.choice([0,1,2]))
