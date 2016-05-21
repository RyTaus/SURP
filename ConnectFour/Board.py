class GameBoard:

    def __init__(self):
        self.height = 6
        self.width = 7

        self.board = [["-" for i in range(self.height)] for j in range(self.width)]
        self.pieces = ["X", "O"]
        self.turnNumber = 0
        self.lastPosition = [None, None]


    def switch_turn(self):
        self.turnNumber = (self.turnNumber + 1) % 2

    def print_board(self):
        board = ""
        for i in range(self.height):
            for j in range(self.width):
                board += self.board[j][self.height - 1 - i]
            board +="\n"

        print(board)

    def to_string_one_line(self):
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s = s + self.board[j][i]
        return s

    def set_coord(self, col, piece):
        rowCoord = self.height - self.board[col].count("-")
        self.lastPosition = (col, rowCoord)
        self.board[col][rowCoord] = piece

    def place_piece(self, col):
        self.set_coord(col, self.pieces[self.turnNumber])

    def valid_actions(self):
        validCols = []
        for col in range(7):
            if self.board[col].count("-") > 0:
                validCols.append(col)
        return validCols

    def is_valid_action(self, col):
        return col in self.valid_actions()

    def is_tie(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == "-":
                    return False 
        return True

    def has_won_vertically(self, piece):
        col = self.lastPosition[0]
        row = self.lastPosition[1]
        # if self.lastPosition[1] < 3:
        #     if piece == self.board[col][row] == self.board[col][row+1] == \
        #     self.board[col][row+2] == self.board[col][row+3]:
        #         return True

        # return False

        rows = [row - 1, row - 2, row - 3]
        if any([r < 0 for r in rows]):
            return False
        return all([self.board[col][r] == self.board[col][row] for r in rows])

    def has_won_horizontally(self, piece):
        col = self.lastPosition[0]
        row = self.lastPosition[1]
        # whichCol = 0
        # if col > 0:
        #     while ((col - whichCol) >= 0 and self.board[col - whichCol][row] == piece):
        #         whichCol += 1
        # print(self.lastPosition)
        # if piece == self.board[col+1 - whichCol][row] == self.board[col+2 - whichCol][row] == \
        # self.board[col+3 - whichCol][row] == self.board[col+4 - whichCol][row]:
        #     return True

        # return False
        cols = [[col - 3, col - 2, col - 1], [col - 2, col - 1, col + 1], [col - 1, col + 1, col + 2], [col + 1, col + 2, col + 3]]

        for cl in cols:
            if any([c < 0 or c >= self.width for c in cl]):
                pass
            else:
                if all([self.board[c][row] == self.board[col][row] for c in cl]):
                    return True
        return False



    def has_won(self, piece):
        if self.has_won_vertically(piece) or self.has_won_horizontally(piece):
            return True

        return False

    def copy(self):
        copy = GameBoard()
        for i in range(self.height):
            for j in range(self.width):
                copy.board[j][i] = self.board[j][i]
        return copy

    def get_results(self):
        return None