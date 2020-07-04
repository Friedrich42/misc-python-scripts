class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_all(self):
        print(self.name + " " + str(self.age), end='')

class Mudak(Person):
    def __init__(self, name, age, mudak_li=1):
        super().__init__(name, age)
        self.mudak_li = mudak_li

    def display_all(self):
        super().display_all()
        print(" " + str(bool(self.mudak_li)))

p = Mudak("Fri", 21, "Тот еще мудила")
p.display_all()
