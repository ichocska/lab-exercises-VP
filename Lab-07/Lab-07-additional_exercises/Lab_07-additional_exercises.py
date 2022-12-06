import random


# Exercise 2
class InvalidParameterError(Exception):
    def __init__(self, message="One or more than one of the provided parameters aren't from type float"):
        super().__init__(message)
        print(message)


class NutrientError(Exception):
    def __init__(self, message="Sum of nutrients is greater than 100"):
        super().__init__(message)
        print(message)


class InvalidFoodError(Exception):
    def __init__(self, message="All parameters are equal to 0"):
        super().__init__(message)
        print(message)


# carbs, protein, fats, salt -> float
class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)

        if type(self.carbs) != float or type(self.protein) != float or type(self.fats) != float or type(
                self.salt) != float:
            raise InvalidParameterError
        elif (self.carbs + self.protein + self.fats + self.salt) > 100.0:
            raise NutrientError
        elif self.carbs == 0 and self.protein == 0 and self.fats == 0 and self.salt == 0:
            raise InvalidFoodError

    def print_label(self):
        print(f"Food: ({self.carbs}, {self.protein}, {self.fats}, {self.salt})")


# for i in range(0, 120, 10):
# try:
# food = Food(i, i, i, i)
# food.print_label()
# except Exception as ex:
# print(f"{ex}")


# Exercise 3
class InvalidParameter(Exception):
    def __init__(self, name):
        super().__init__(name)
        print(f"Invalid class parameter: {name}", end='')


class InvalidAgeError(InvalidParameter):
    def __init__(self):
        print(f"Invalid class parameter: age", end='')



class InvalidSoundError(InvalidParameter):
    def __init__(self):
        print(f"Invalid class parameter: sound", end='')


# name, sound -> str
# age -> int
class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if type(self.name) != str:
            raise InvalidParameter
        if type(self.age) != int:
            raise InvalidAgeError
        if type(self.sound) != str:
            raise InvalidSoundError

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self, *args):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError
        if sound.count("r") < 2:
            raise InvalidSoundError


    def print(self):
        print(f"Jaguar {self.name}, {self.age}, {self.sound}")

    def daily_task(self, animals):
        for x in animals:
            if type(x) == Lemur or type(x) == Human:
                animals.remove(x)
            print(f"{self.name} the Jaguar hunted down {x.name} the {x.__class__.__name__}")


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError
        if "e" not in sound:
            raise InvalidSoundError

        super().__init__(name, age, sound)

    def print(self):
        print(f"Lemur: {self.name}, {self.age}, {self.sound}")

    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits - 10
        elif fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        elif fruits <= 0:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError
        if "e" not in sound:
            raise InvalidSoundError

        super().__init__(name, age, sound)

    def print(self):
        print(f"Human: {self.name}, {self.age}, {self.sound}")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if type(animals[i]) == Human:
                if i == 0:
                    if type(animals[i + 1]) == Human:
                        buildings.append(Building("House"))
                elif i == len(animals)-1:
                    if type(animals[i - 1]) == Human:
                        buildings.append(Building("House2"))
                else:
                    if type(animals[i + 1]) == Human and type(animals[i - 1]) == Human:
                        buildings.append(Building("House3"))

# type -> str
class Building:
    def __init__(self, type):
        self.type = type


fruits = 100
animals = []
buildings = []

names = ["Jacob", "David", "Bobby", "Steve", "Johanssen", "Mac", "Jason", "Edward", "Alex", "Maddie", "Susan",
         "Abigail", "Jessica",
         "Lizzy", "Monica", "Lorelei", "Sandra", "Michelle"]

sounds = ["RAAWR", "ROAR", "Grrr", "Shriek", "Meow", "Eeek", "Aaaaa", "Speak", "I am a Human"]

for i in range(102):
    number = random.randint(0, 9)
    if 0 <= number <= 3:
        index_of_name = random.randint(0, len(names) - 1)
        age = random.randint(7, 20)
        index_of_sounds = random.randint(0, len(sounds) - 1)
        try:
            lemur = Lemur(names[index_of_name], age, sounds[index_of_sounds])
            animals.append(lemur)
        except Exception as ex:
            print(ex)
    elif 4 <= number <= 7:
        index_of_name = random.randint(0, len(names) - 1)
        age = random.randint(7, 20)
        index_of_sounds = random.randint(0, len(sounds) - 1)
        try:
            jaguar = Jaguar(names[index_of_name], age, sounds[index_of_sounds])
            animals.append(jaguar)
        except Exception as ex:
            print(ex)
    elif 8 <= number <= 9:
        index_of_name = random.randint(0, len(names) - 1)
        age = random.randint(7, 20)
        index_of_sounds = random.randint(0, len(sounds) - 1)
        try:
            human = Human(names[index_of_name], age, sounds[index_of_sounds])
            animals.append(human)
        except Exception as ex:
            print(ex)

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(f"Animals List: {animals}")
print(f"Buildings List: {buildings}")
