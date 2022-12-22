class Item(object):
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    def __repr__(self):
        return f'Item: {self.name} {self.durability}'

    def __str__(self):
        return self.__repr__()

    def print(self):
        return self.__repr__()
