class Board:
    def __init__(self, board):
        self.board = board

    def convert_letters():
        convert_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        return convert_to_num

    def print(self):
        print("  A B C D E F")
        rows = 1
        for row in self.board:
            print(rows, " ".join(row))
            rows += 1
        print("-" * 14)


class ships:
    def __init__(self, board):
        self.board = board

    def add_ships(self):
        for i in range(3):
            self.x, self.y = random.randint(0, 5), random.randint(0, 5)
            while self.board[self.x][self.y] == "X":
                self.x, self.y = random.randint(0, 5), random.randint(0, 5)
            self.board[self.x][self.y] = "X"
        return self.board

    
