# %% [md]
# # Polymorphism
# * Polymorphism simply means to change.
# * In the context of OOP, it means that a derived class can change the behavior of a base class

# %% [md]
# # Derived Class
# Example of defining a base and derived class
# * In this example, class Birds and Sloths derive from Animal
# * In other words, Bird is an Animal and Sloth is an Animal

# %% codecell
class Animal():
    pass

class Bird(Animal):
    pass

class Sloth(Animal):
    pass

# %% [md]
# # Behavior
# * We give animals the ability to move
# * This is defined in the base class
# * Therefore all animals, including Birds and Sloths can move

# %% codecell
class Animal():
    def move(self):
        print('Moving')

class Bird(Animal):
    pass

class Sloth(Animal):
    pass

# %% codecell
a = Animal()
a.move()

b = Bird()
b.move()

s = Sloth()
s.move()

# %% [md]
# # Polymorphism
# * Birds and Sloths move differently
# * We can override or change behavior for specific animals using polymorphism

# %% codecell
class Animal():
    def move(self):
        print('Moving')

class Bird(Animal):
    def move(self):
        print('Flying')

class Sloth(Animal):
    def move(self):
        raise Exception('Not Happening')

# %% codecell
a = Animal()
a.move()

b = Bird()
b.move()

s = Sloth()
s.move()

# %% [md]
# # Recall Aminals, Dogs & Cats

# %% codecell
class Animal():
    def __init__(self, lives=1):
        self.lives = lives

class Dog(Animal):
    def __init__(self):
        super().__init__(lives=1)
        
    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self):
        super().__init__(lives=9)

    def sound(self):
        return "Meow"

# %% [md]
# # Refactor Aminals, Dogs & Cats
# We want to push the definition of sound into our base class since it 
# pertains to both cats and dogs (and presumably any animal)
# We want ot override the behavior in our derived classes.

# %% codecell
class Animal():
    def __init__(self, lives=1):
        self.lives = lives
        
    def sound(self):
        return "Sound"

class Dog(Animal):
    def __init__(self):
        super().__init__(lives=1)
        
    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self):
        super().__init__(lives=9)

    def sound(self):
        return "Meow"

# %% codecell
animal = Animal()
print(animal.sound())

dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())
