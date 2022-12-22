from enum import Enum
from entities import errors
from entities import weapon
from entities import item


class Character(object):
    names = []

    def __init__(self, name, gender, ch_class, main_weapon: weapon.Weapon, additional_item: item.Item):
        if name in self.names:
            raise errors.CharacterExists('Already Exists')
        self.name = name
        self.gender = gender
        self.ch_class = ch_class
        self.main_weapon = main_weapon
        self.additional_item = additional_item
        self.names.append(name)

    def __repr__(self):
        weapon_info = ""
        item_info = ""
        if self.main_weapon is not None:
            weapon_info = self.main_weapon.print()
        if self.additional_item is not None:
            item_info = self.additional_item.print()
        return f"Character: {self.name} {self.gender} {self.ch_class} {weapon_info} {item_info}"

    def GetList(self):
        return self.names

    def print(self):
        return self.__repr__()


class HeroClass(Enum):
    Rogue = 'Rogue',
    Mage = 'Mage',
    Priest = 'Priest',
    Warrior = 'Warrior'
