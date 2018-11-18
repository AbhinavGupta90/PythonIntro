class Player():
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count():
        return Player.count

player1 = Player("Messi")
player2 = Player("Pele")
player3 = Player("Ronaldo")
player4 = Player("Zidane")

print(player1.count)
print(player2.count)
print(player3.count)
player4.count = 100
print(player4.count)
Player.count = 12
print(Player.count)
print(player4.get_count())#can call the static method even if it's an instance
print(player2.get_count())
print(Player.get_count())

