# %% [md]
# # Abstract Base Classes
# Abstract base classes enforce rules in inheritence

# %% codecell
from abc import ABC
from abc import abstractmethod

# %% [md] 
# # Abstract Base Class
# * You can inherit from an ABC, but you can't create an instance of one
# * It can define abstract methods, that derived classes must implment
# * It can have concrete methods (and properties) that derived methods inherit

# %% codecell

class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def park(self):
        pass
        
# %% codecell
vehicle = Vehicle()

# %% [md]
# # Derived Classes

class Car(Vehicle):
    
    def move(self):
        print('Driving')
        
    def park(self):
        print('Garage')
       
        
class Airplane(Vehicle):
    
    def move(self):
        print('Flying')
        
    def park(self):
        print('Hangar')
        
# %% codecell
car = Car()
car.move()
car.park()

airplane = Airplane()
airplane.move()
airplane.park()

# %% [md]
# # Abstract Methods must have a concrete implementation
# * Let's create a ship, with only move implemented
# * We get an exception - park isn't implemented

# %% codecell
class Ship(Vehicle):
    
    def move(self):
        print('Sailing')

# %% codecell
ship = Ship()


# %% [md]
# # Behavior in Abstract Classes
# * Our Vehicle class keeps a speed int
# * We can accelerate and stop

# %% codecell
class Vehicle(ABC):
    
    def __init__(self):
        self._speed = 0
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def park(self):
        pass
    
    def accelerate(self, amount):
        self._speed += amount
        
    def stop(self):
        self._speed = 0
        
# %% [md]
# # Derived Classes

class Car(Vehicle):
    
    def move(self):
        print(f'Driving {self._speed} miles')
        
    def park(self):
        print('Garage')
       
        
class Airplane(Vehicle):
    
    def move(self):
        print(f'Flying {self._speed} miles')
        
    def park(self):
        print('Hangar')
        
        
# %% codecell
car = Car()
car.accelerate(60)
car.move()
car.park()
car.stop()

airplane = Airplane()
airplane.accelerate(450)
airplane.move()
airplane.park() 
airplane.stop()

# %% codecell
fleet = []
fleet.append(Car())
fleet.append(Airplane())
fleet.append(Car())

for vehicle in fleet:
    vehicle.accelerate(50)
    vehicle.move()