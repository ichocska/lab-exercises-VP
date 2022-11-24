class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"{self.name}, {self.family}, {self.nationality}")


#yearofstudy -> година на обучение
class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(f"{self.name}, {self.family}, {self.age}, {self.nationality}, {self.university}, {self.year_of_study}")


#experience -> години преподавателски стаж
class Lecture(Person):
    def __init__(self,name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print(f"{self.name}, {self.family}, {self.age}, {self.nationality}, {self.university}, {self.experience}")


my_person = Person("Ivailo", "Nikolov", 19, "Bulgaria")
my_person1 = Student("Ivailo", "Nikolov", 19, "Bulgaria", "Tu Sofia", 1)
my_person2 = Lecture("Ivan", "Ivanov", 26, "Bulgaria", "Tu Sofia", 3)
my_person.print()
my_person1.print()
my_person2.print()
