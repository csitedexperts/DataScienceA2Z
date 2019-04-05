## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ that takes two parameters: seld and name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes two  parameters: self and name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes two parameters self, and name?
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## class Employee has-a __init__ that takes three parameters: self, name, and salary
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## ?Salmon is-a Fish
class Salmon(Fish):
    pass

## Halbit is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get pet and set it to satan
mary.pet = satan



## frank is-a Employee with attribute name = "Frank" and salary = 120000
frank = Employee("Frank", 120000)

## from frank get pet attribute and set to rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
