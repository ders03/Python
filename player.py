

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return self.name + ":" + str(self.health)

    def attack(self, p):
        p.health -= 40
        if p.health < 0:
            p.health = 0

class Creep(Player):
    def __init__(self):
        super().__init__("Creeper")
        self.health = 30

    def attack(self, p):
        p.health -= 7
        if p.health<0:
            p.health = 0


def main():
    p1 = Player("test")
    p2 = Player("test2")
    print(p1)

if __name__ == "__main__":
    main()
