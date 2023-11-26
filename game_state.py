from numpy import ndarray

class Board():
    """Board class made to store the current game state of the tictactoe board; 
    search and evaluation classes will be stored in seperate files"""    
    
    def __init__(self):
        """The constructor will initialize the board with empty values
        The entire game state of the board is being stored as a python list."""
        self.board = ([
            ["","",""],
            ["","",""],
            ["","",""]
        ])
        
    def visualize_board(self,boards):
        """This function is useful for displaying the game onto the console for now;
        In future implementations, this console centric display will be replaced with a GUI"""

        print()
        print(f" {boards[0][0]} | {boards[0][1]} | {boards[0][2]} ")
        print("---+---+---")
        print(f" {boards[1][0]} | {boards[1][1]} | {boards[1][2]} ")
        print("---+---+---")
        print(f" {boards[2][0]} | {boards[2][1]} | {boards[2][2]} ")
        print()

b = Board()
b.visualize_board(b.board)