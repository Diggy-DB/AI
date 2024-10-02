class Animal:
    def super(self):
        print("This is an Animal class")
class Dog(Animal):
    def __init__(self):
        self.name = "Dog"
        self.type = "Mammal"
    def print_info(self):
        print("This is a " + self.name)
        print("It is a type of " + self.type)
        d.super()

d = Dog()
d.print_info()
print(isinstance(d, Animal))
print(issubclass(Dog, Animal))