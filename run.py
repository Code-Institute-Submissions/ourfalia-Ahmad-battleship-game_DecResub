import random


class Board:
    def __init__(self, board):
        self.board = board

    # def convert_letters():
    #     convert_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
    #     return convert_to_num

    def print(self):
        #print("  A B C D E F")
        print("  1 2 3 4 5 6") 
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

    def make_guess(self):
        while True:
            try:
                x = int(input("Please pick a row number:\n"))
                while not 0 < x < 7:
                    raise ValueError()
                y = int(input("Please pick a column number:\n"))
                while not 0 < y < 7:
                    raise ValueError()
            except ValueError:
                print("Please enter a number between 1 and 6")
            else:  
                return int(x) -1, int(y) -1


    def score(self):
        score = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    score += 1
        return score


def new_game():
    computer = Board([["."] * 6 for i in range(6)])
    guesses = Board([["."] * 6 for i in range(6)])
    ships.add_ships(computer)
    # set 18 attempts
    turns = 18
    while turns > 0:
        Board.print(guesses)
        # get the player's input
        x, y = ships.make_guess(object)
        # check if there is any duplication
        while guesses.board[x][y] != ".":
            print("-" * 14)
            print("You already picked that one! \n")
            x, y = ships.make_guess(object)
        # check if the player scores or misses 
        if computer.board[x][y] == "X":
            print("-" * 14)
            print("Well done, you hit a battleship! \n")
            guesses.board[x][y] = "X"
        else:
            print("-" * 14)
            print("You missed, try again! \n")
            guesses.board[x][y] = "-"
        # check for the final score 
        if ships.score(guesses) == 3:
            print("-" * 14)
            print("Congratulations, You hit all the battleships! \n")
            break
        else:
            turns -= 1
            print(f"Only {turns} tries left \n")
            if turns == 0:
                print("Sorry, game is over! \n")
                Board.print(guesses)
                break


new_game()
