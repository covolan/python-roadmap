from os import system

class Board:
    
    def __init__(self, board_data = list()) -> None:
        self.board_data = board_data
    
    def InitBoard(self, data = 9 * ['n']):
        self.board_data = data

    def ClearBoard(self):
        for i, j in enumerate(self.board_data):
            if (j != 'n'):
                self.board_data[i] = 'n'

    def ClearScreen(self):
        system("clear")
    
    def AssingDataToBoard(self, symb, pos):
        if (self.board_data[pos] == 'n' and (symb == 'x' or symb == 'o')):
            self.board_data[pos] = symb
        else:
            print("not a valid position or symbol, try again")
            self.AssingDataToBoard(symb, int(input()) - 1)

    def PrintBoard(self):
        print(f"-1-|-2-|-3-\n {self.board_data[0]} | {self.board_data[1]} | {self.board_data[2]} \n-4-|-5-|-6-\n {self.board_data[3]} | {self.board_data[4]} | {self.board_data[5]} \n-7-|-8-|-9-\n {self.board_data[6]} | {self.board_data[7]} | {self.board_data[8]} ")

    def CheckBoard(self):
        if (self.board_data[0] == 'x' and self.board_data[1] == 'x' and self.board_data[2] == 'x') or (self.board_data[3] == 'x' and self.board_data[4] == 'x' and self.board_data[5] == 'x') or (self.board_data[6] == 'x' and self.board_data[7] == 'x' and self.board_data[8] == 'x') or (self.board_data[0] == 'x' and self.board_data[3] == 'x' and self.board_data[6] == 'x') or (self.board_data[1] == 'x' and self.board_data[4] == 'x' and self.board_data[7] == 'x') or (self.board_data[2] == 'x' and self.board_data[5] == 'x' and self.board_data[8] == 'x') or (self.board_data[0] == 'x' and self.board_data[4] == 'x' and self.board_data[8] == 'x') or (self.board_data[2] == 'x' and self.board_data[4] == 'x' and self.board_data[6] == 'x'):
            return 'x'
        if (self.board_data[0] == 'o' and self.board_data[1] == 'o' and self.board_data[2] == 'o') or (self.board_data[3] == 'o' and self.board_data[4] == 'o' and self.board_data[5] == 'o') or (self.board_data[6] == 'o' and self.board_data[7] == 'o' and self.board_data[8] == 'o') or (self.board_data[0] == 'o' and self.board_data[3] == 'o' and self.board_data[6] == 'o') or (self.board_data[1] == 'o' and self.board_data[4] == 'o' and self.board_data[7] == 'o') or (self.board_data[2] == 'o' and self.board_data[5] == 'o' and self.board_data[8] == 'o') or (self.board_data[0] == 'o' and self.board_data[4] == 'o' and self.board_data[8] == 'o') or (self.board_data[2] == 'o' and self.board_data[4] == 'o' and self.board_data[6] == 'o'):
            return 'o'
        if not('n' in self.board_data):
            return 'd'
        return 'n'

# Main game loop
tictactoe = Board()

tictactoe.InitBoard()
while True:
    tictactoe.PrintBoard()
    print("X turn [x, position]: ")
    tictactoe.AssingDataToBoard('x', int(input()) - 1)
    tictactoe.ClearScreen()
    TEMPCHECK = tictactoe.CheckBoard()
    if (TEMPCHECK in ('x', 'o', 'd')):
        tictactoe.PrintBoard()
        print(f"{TEMPCHECK.upper()} Won the game, continue [y/n]? ")
        cont = input().lower()
        if (cont == "n"):
            break
        tictactoe.ClearScreen()
        tictactoe.ClearBoard()
        continue
    tictactoe.PrintBoard()
    print("O turn [o, position]: ")
    tictactoe.AssingDataToBoard('o', int(input()) - 1)
    tictactoe.ClearScreen()
    TEMPCHECK = tictactoe.CheckBoard()
    if (TEMPCHECK in ('x', 'o', 'd')):
        tictactoe.PrintBoard()
        print(f"{TEMPCHECK.upper()} Won the game, continue [y/n]? ")
        cont = input().lower()
        if (cont == "n"):
            break
        tictactoe.ClearScreen()
        tictactoe.ClearBoard()
        continue
    tictactoe.ClearScreen()
    TEMPCHECK = ''

