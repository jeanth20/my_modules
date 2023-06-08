class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
    def hp_value(self):
        return self.hp

    def attack(self, target):
        target.hp -= self.damage
        print(f"{self.name} attacked {target.name} for {self.damage} damage")
        print(f"{target.name} has {target.hp} hp left")

    @staticmethod
    def new_game():
        print("\n ---New game--- \n")


Monster.new_game()
bigmonster = Monster("Big Monster", 100, 50)
smallmonster = Monster("Small Monster", 50, 10)

smallmonster.attack(bigmonster)
smallmonster.attack(bigmonster)
smallmonster.attack(bigmonster)

bigmonster.attack(smallmonster)


Monster.new_game()
centaur = Monster("Centaur", 200, 100)
goblin = Monster("Goblin", 50, 10)

centaur.attack(goblin)
goblin.attack(centaur)