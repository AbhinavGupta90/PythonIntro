from abc import ABC, abstractmethod


class GamingConsole(ABC):

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

class MarioGame(GamingConsole):

    def up(self):
        print("Goes up")

    def left(self):
        print("Goes left")

    def right(self):
        print("Goes right")

    def down(self):
        print("Goes down")

class ChessGame(GamingConsole):

    def up(self):
        print("A piece is moving up")

    def left(self):
        print("A piece is moving left")

    def right(self):
        print("A piece is moving right")

    def down(self):
        print("A piece is moving down")


console = MarioGame()
console.up()
console.up()
console.right()
console.down()

poly_console = [MarioGame(), ChessGame()]

for console in poly_console:
    console.down()
    console.right()
    console.left()
    console.up()

