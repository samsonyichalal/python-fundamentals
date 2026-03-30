# This program shows how constructors (__init__)
# are used to initialize object attributes.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Samson", 21)
student2 = Student("Sara", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)