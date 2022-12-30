from random import randint

from . import constants


class BoardItem:
    """
    This class represents the different stationary board items like the snake and the ladder.
    We may have different classes of Ladder and Snake to denote them as well but we have a workaround.
    We would use constants (or enums) to denote the ladder or the snake as the item on the board.
    """

    def __init__(self, item: str, start: int, end: int) -> None:
        self.item: str = item
        self.start: int = start
        self.end: int = end

    def __str__(self) -> str:
        if self.item == constants.ITEM_SNAKE:
            return "This snake demotes players from %d to %d" % (self.start, self.end)
        elif self.item == constants.ITEM_LADDER:
            return "This snake promotes players from %d to %d" % (self.start, self.end)


class Cell:
    """
    This class represents the single cell in a snake and ladder game (typically there are a hundred).
    The reason of creating this class is to not leave out any real-world objects from an abstract software representation in code.
    This class is optional. We can instead just have the main array on the board.
    The reason why it is good to have is because additional logic and extrapolations can easily be done on it.
    """

    def __init__(self) -> None:
        self.board_item: BoardItem = None

    def __str__(self) -> str:
        if self.board_item:
            return "This is a cell on the board having the item %s." % self.board_item.item
        return "This is a cell on the board having no items."


class Board:
    """
    This class represents the entire game board which is composed of n cells.
    The cells may be represented as simple valued lists as well as objects of the Cell class.
    """

    def __init__(self, number_of_cells: int=100, number_of_snakes: int=5, number_of_ladders: int=5) -> None:
        self.number_of_cells: int = number_of_cells
        self.number_of_snakes: int = number_of_snakes
        self.number_of_ladders: int = number_of_ladders
        self.cells: list = list()
        self.__create_cells()
        self.__create_items(constants.ITEM_LADDER)
        self.__create_items(constants.ITEM_SNAKE)

    def __str__(self) -> str:
        return "This is the game board representing %d squares." % self.number_of_cells

    def __create_cells(self) -> None:
        """This method creates the board by placing in the cells."""
        for cell in range(self.number_of_cells):
            self.cells[cell] = Cell()

    def __create_items(self, constant) -> None:
        """This method places in the items (snakes and ladders)."""
        looper: int = self.number_of_snakes if constant == constants.ITEM_SNAKE else self.number_of_ladders
        while looper > 0:
            start: int = randint(0, self.number_of_cells)
            end: int = randint(0, self.number_of_cells)
            if (end > start and constant == constants.ITEM_SNAKE) or (end < start and constant == constants.ITEM_LADDER):
                continue
            item = BoardItem(constants.ITEM_SNAKE, start, end) if constant == constants.ITEM_SNAKE else BoardItem(constants.ITEM_LADDER, start, end)
            self.cells[start].board_item = item
            looper -= 1

    def get_player_cell(self, player_position: int) -> Cell:
        """This method is used to get the Cell at the player's position."""
        return self.cells[player_position]


class Dice:
    """
    This class represents the dice for the game.
    """

    def __init__(self, count: int=1) -> None:
        self.count: int = count

    def __str__(self) -> str:
        if self.count == 1:
            return "There is only one dice for this game."
        return "There are %d dice for this game." % self.count

    def roll(self) -> int:
        total_rolls: int = 0
        for _ in range(self.count):
            total_rolls += randint(constants.MINIMUM_FACE, constants.MAXIMUM_FACE)
        return total_rolls


class Player:
    """
    This class represents the player.
    """

    def __init__(self, name: str=None, current_position: int=0) -> None:
        self.id: int = randint(constants.MINIMUM_ID, constants.MAXIMUM_ID)
        self.name: str = name
        self.current_position: int = current_position

    def __str__(self) -> str:
        return "This is the player %s with ID as %d." % (self.name, self.id)


class Game:
    """
    This class represents the entire game.
    """

    def __init__(self, player_count: int=2) -> None:
        self.board: Board = Board()
        self.dice: Dice = Dice()
        self.player_count: int = player_count
        self.player: list = list()
        self.winner: Player = None
        self.__set_players()
        self.__set_attributes()

    def __set_attributes(self):
        """This is to set up the attrobutes of all other parameters of the game."""
        dice_count = int(input("Enter the number of dice: "))
        self.dice.count = dice_count

    def __set_players(self):
        """This is to create the players."""
        for iterator in range(self.player_count):
            name = input("Enter player %d name: " % self.player_count)
            self.player[iterator] = Player(name=name)

    def start(self):
        """This starts up the game."""
        while not self.winner:
            for iterator in range(self.player_count):
                print("%s's turn." % self.player[iterator])
                dice_roll = self.dice.roll()
                print("Dice roll: %d. Previous position: %d. Current position: %d." % (dice_roll, self.player[iterator].current_position, self.player[iterator].current_position + dice_roll))
                self.player[iterator].current_position += dice_roll
                if self.player[iterator].current_position == self.board.number_of_cells:
                    self.winner = self.player[iterator]
                    break
                if self.board.cells[self.player[iterator].current_position].board_item.item == constants.ITEM_LADDER:
                    self.player[iterator].current_position = self.board.cells[self.player[iterator].current_position].board_item.end
                    print("Player got promoted by a ladder! Current position: %d" % self.player[iterator].current_position)
                if self.board.cells[self.player[iterator].current_position].board_item.item == constants.ITEM_SNAKE:
                    self.player[iterator].current_position = self.board.cells[self.player[iterator].current_position].board_item.end
                    print("Player got bit by a snake! Current position: %d" % self.player[iterator].current_position)
        print("The winner is: %s!" % self.winner.name)


if __name__ == "__main__":
    game = Game()
    game.start()
