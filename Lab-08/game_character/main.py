from entities.character import Character
from entities.character import HeroClass
from entities.weapon import Weapon
from entities.item import Item
from entities.errors import *


class Menu:
    heroes_list = []

    def run(self):
        # infinite menu loopa
        while True:
            self.PrintMenu()
            # ask the user to choose a command
            choice = int(input("Choose an item from the menu: \n> "))
            if choice == 6:
                break
            # catch errors
            try:
                # process the user's choice
                if type(choice) == int and 5 >= choice > 0:
                    self.MenuAction(choice)
                else:
                    raise Exception("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

    def PrintMenu(self):
        print('==========MENU===============')
        print('Option 1: Create new Hero')
        print('Option 2: Create new Weapon for already Existing Hero')
        print('Option 3: Create new Item for already Existing Hero')
        print('Option 4: Print All Heroes')
        print('Option 5: Delete A Hero')
        print('Option 6: Exit')

    def MenuAction(self, command_number: int):
        if command_number == 1:
            self.CreateHero()
        elif command_number == 2:
            self.CreateAWeaponForAHero()
        elif command_number == 3:
            self.CreateAnItemForAHero()
        elif command_number == 4:
            self.PrintAllHeroes()
        elif command_number == 5:
            self.DeleteAHero()

    def CreateHero(self):
        name = input('Please enter the name of the Hero:')
        gender = input('Please enter the gender of the Hero (len at least 4, only letters):')
        if len(gender) < 4 or not gender.isalpha():
            raise InvalidCharacterClass('Not a valid gender!')
        ch_class = input('Please enter the class of the Hero (len at least 4, only letters):')
        acceptable_class_values = [x.value for x in HeroClass]

        if (ch_class,) not in acceptable_class_values:
            raise InvalidCharacterClass('This class does not exist')
        person = Character(name, gender, ch_class, None, None)
        self.heroes_list.append(person)

    def CreateAWeaponForAHero(self):
        hero_name = input('Please enter the name of the hero:')
        if hero_name not in Character.GetList(Character):
            raise CharacterNotFound('This Hero does not exist!')
        name = input('Please enter the name of the Weapon (len at least 4, only letters):')
        dmg = int(input('Please enter the damage of the Weapon:'))
        if dmg < 0:
            raise InvalidItemError('This item is invalid!')
        for x in self.heroes_list:
            if x.name == hero_name:
                x.mainWeapon = Weapon(name, 100, dmg)
                return

    def CreateAnItemForAHero(self):
        hero_name = input('Please enter the name of the hero:')
        if hero_name not in Character.GetList(Character):
            raise CharacterNotFound('This Hero does not exist!')
        name = input('Please enter the name of the Item (len at least 4, only letters):')
        for x in self.heroes_list:
            if x.name == hero_name:
                x.mainWeapon = Item(name, 100)
                return

    def PrintAllHeroes(self):
        for x in self.heroes_list:
            print(x)

    def DeleteAHero(self):
        hero_name = input('Please enter the name of the hero:')
        if hero_name not in Character.GetList(Character):
            raise CharacterNotFound('This Hero does not exist!')
        for x in range(len(self.heroes_list)):
            if self.heroes_list[x].name == hero_name:
                del self.heroes_list[x]
                del Character.GetList(Character)[x]


if __name__ == '__main__':
    menu = Menu()
    menu.run()
