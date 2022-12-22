from entities import item


class Weapon(item.Item):
    def __init__(self, name, durability, dmg):
        self.attack = dmg
        super().__init__(name, durability)

    def print(self):
        return f"Weapon: {self.name} {self.attack} {self.durability}"
