class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def tellage(self):
        print(self.age)
    def sayName(self):
        print(self.firstName + ' ' + self.lastName)
p = Person("Delger", "Byambasukh", 21)
p.tellage()
p.sayName()
 