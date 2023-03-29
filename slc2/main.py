"""Создайте класс Human, который будет содержать 
информацию о человеке.
С помощью механизма наследования, реализуйте класс 
Builder (содержит информацию о строителе), класс Sailor 
(содержит информацию о моряке), класс Pilot (содержит 
информацию о летчике).
Каждый из классов должен содержать необходимые 
для работы методы."""

class Human():
    counter = 0

    def __init__(self, name):
        Human.counter = self.counter + 1
        self._name = name

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getCounter(self):
        return Human.counter
    
    def out(self):
        print("Human = ", self._name)

class Builder(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        Builder.counter = self.counter + 1
        self.__prof = prof

    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCounter(self):
        return Builder.counter
    
    def out(self):
        print("Builder = ", self.__prof)

class Sailor(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        Sailor.counter = self.counter + 1
        self.__prof = prof

    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCounter(self):
        return Sailor.counter
    
    def out(self):
        print("Sailor = ", self.__prof)

class Pilot(Human):
    counter = 0

    def __init__(self, name, reis):
        super().__init__(name)
        Pilot.counter = self.counter + 1
        self.__reis = reis

    def getreis(self):
        return self.__reis
    
    def setreis(self, reis):
        self.__reis = reis

    def getCounter(self):
        return Pilot.counter
    
    def out(self):
        print("Pilot = ", self.__reis)

list  = [Human("User"), Builder("builder", "welder"), Sailor("Jack", "Cap"), Pilot("Ivan", 100), Pilot("Sergey", 1200)]

def out(list):
    for el in list:
        el.out()

out(list)
print('--------------------------------------------')
def getCounter(list):
    for el in list:
        print(el.getCounter())

getCounter(list)