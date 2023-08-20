from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, firstName, lastName):
        self.fistName = firstName
        self.lastName = lastName
        
    @staticmethod
    def calculateSalary():
        return 1000
        
class Employee(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.id = id

class FullTimeEmployee(Employee):
    def __init__(self, firstName, lastName, benefits):
        super().__init__(id, firstName, lastName)
        self.benefits = benefits
        
persons = [
    Employee(100, 'A', 'B'),
    Employee(200, 'C', 'D'),
    FullTimeEmployee(300, 'X', 'Y'),

]