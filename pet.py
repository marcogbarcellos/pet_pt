# resources:
#   https://docs.python.org/3/tutorial/classes.html
#   https://www.tutorialspoint.com/python/python_classes_objects.htm
#   https://learnpythonthehardway.org/book/ex40.html
from random import randrange

class Pet:

    fome_reduce = 3
    fome_max = 10
    fome_warning = 2
    sono_reduce = 2
    sono_max = 10
    sono_warning = 3
    sede_reduce = 2
    sede_max = 10
    sede_warning = 3

    vocab = ['"grrr..."', '"estou com fome"',
             '"estou com sede"', '"estou com sono"']
    # expects to be instantiated using a dictionary like ...
    # pet = Pet({'name':'Kirby', 'type':'Dog', 'age':'really old'})

    def __init__(self, options):
        self._name = options['name']
        self._animal_type = options['type']  # e.g. 'Dog', 'Cat' and 'Bird'
        self._age = options['age']
        self.fome = randrange(self.fome_max)
        self.sono = randrange(self.sono_max)
        self.sede = randrange(self.sede_max)
        self.vocab = self.vocab[:]

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def set_animal_type(self, new_type):
        self._animal_type = new_type

    def set_age(self, new_age):
        self._age = new_age

    @property
    def mood(self):
        if self.fome > self.fome_warning and self.sono > self.sono_warning and self.sede > self.sede_warning:
            return "happy"
        elif self.fome < self.fome_warning:
            return "com fome"
        elif self.sono < self.sono_warning:
            return "cansado"
        else:
            return "com sede"

    def __clock_tick(self):
        self.fome -= 1
        self.sono -= 1
        self.sede -= 1

    def talk(self):
        print("eu sou um ", self.animal_type,)
        self .__clock_tick()

    def feed(self):
        print("hmmm, obrigado")
        meal = randrange(self.fome, self.fome_max)
        self.food += meal
        if self.food < 0:
            self.food = 0
            print("eu estou com fome")
        elif self.fome > self.fome_max:
            self.fome = self.fome_max
            print("nao estou com fome mais")
        self .__clock_tick()

    def sleep(self):
        print("putting to sleep")
        energy = randrange(self.sono, self.sono_max)
        self.sono += energy
        if self.sono < 0:
            self.sono = 0
            print("estou cansado")
        elif self.sono > self.sono_max:
            self.sono = self.sono_max
            print("nao estou mais cansado")
        self .__clock_tick()
# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type and age of his or her pet.  This data should be stored as the object's attributes.
# Use the object's accessor methods to retrieve the pet's name, type, and age and display this data on the screen.


def main():
    print("----------------")
    print("PETS APPLICATION")
    print("-----------------")

    animal_type = input("Please input the type of pet (e.g. 'Dog'): ")
    name = input("Please input the pet's name (e.g. 'Ruffles'): ")
    age = input("Please input the pet's age in years (e.g. '11'): ")

    pet = Pet({'name': name, 'type': animal_type, 'age': age})

    print(pet._animal_type, pet._name, pet._age)

    choice = None
    while choice != 0:
        print(
            """ 
            **interact with your pet** 
            1- feed your pet 
            2- talk to your pet 
            3- put your pet to sleep 
            4- drink some water 
            0- quit 
            """
        )

        choice = input("choice:")

        if choice == "0":
            print("good bye")
            break
        elif choice == "1":
            pet.feed()
        elif choice == "2":
            pet.talk()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.drink()
        else:
            print("sorry this option isn`t valid")


main()
