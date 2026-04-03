# This program shows how one class can inherit
# properties and methods from another class.

class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog1 = Dog()
dog1.speak()

