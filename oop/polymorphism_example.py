# This program demonstrates polymorphism where
# different classes use the same method name.

class Dog:

    def speak(self):
        print("Dog barks")


class Cat:

    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()