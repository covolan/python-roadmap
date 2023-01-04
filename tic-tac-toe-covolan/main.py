from os import system

class Board:
    
    def __init__(self, board_data = list()) -> None:
        self.board_data = board_data
    
    def initBoard(self, data = 9 * ['n']):
        self.board_data = data

    def clearScreen(self):
        system("clear")
    
    def assingDataToBoard(self, symb, pos):
        if (self.board_data[pos] == 'n' and (symb == 'x' or symb == 'o')):
            self.board_data[pos] = symb
        else:
            print("not a valid position or symbol, try again")
            self.assingDataToBoard()

    def checkBoard(self):
        if (self.board_data[0] == 'x' and self.board_data[1] == 'x' and self.board_data[2] == 'x') or (self.board_data[3] == 'x' and self.board_data[4] == 'x' and self.board_data[5] == 'x') or (self.board_data[6] == 'x' and self.board_data[7] == 'x' and self.board_data[8] == 'x') or (self.board_data[0] == 'x' and self.board_data[3] == 'x' and self.board_data[6] == 'x') or (self.board_data[1] == 'x' and self.board_data[4] == 'x' and self.board_data[7] == 'x') or (self.board_data[2] == 'x' and self.board_data[5] == 'x' and self.board_data[8] == 'x') or (self.board_data[0] == 'x' and self.board_data[4] == 'x' and self.board_data[8] == 'x') or (self.board_data[2] == 'x' and self.board_data[4] == 'x' and self.board_data[6] == 'x'):
            return 'x'
        elif (self.board_data[0] == 'o' and self.board_data[1] == 'o' and self.board_data[2] == 'o') or (self.board_data[3] == 'o' and self.board_data[4] == 'o' and self.board_data[5] == 'o') or (self.board_data[6] == 'o' and self.board_data[7] == 'o' and self.board_data[8] == 'o') or (self.board_data[0] == 'o' and self.board_data[3] == 'o' and self.board_data[6] == 'o') or (self.board_data[1] == 'o' and self.board_data[4] == 'o' and self.board_data[7] == 'o') or (self.board_data[2] == 'o' and self.board_data[5] == 'o' and self.board_data[8] == 'o') or (self.board_data[0] == 'o' and self.board_data[4] == 'o' and self.board_data[8] == 'o') or (self.board_data[2] == 'o' and self.board_data[4] == 'o' and self.board_data[6] == 'o'):
            return 'o'
        elif not('n' in self.board_data):
            return 'd'
        else:
            return 'n'


# Main game loop
if (__name__ == 'main'):
    tictactoe = Board()

    tictactoe.initBoard()

