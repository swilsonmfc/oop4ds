# %% [md]
# # Overview
#
# We cover how to model relationships and behaviors in this class.
# * Is A  = Inheritance
# * Behavior = Functions
# * State = Variables
#
# We model inheritance with classes and base classes.

# %% [md]
# # Example
# Requirements:
# * Dog is an Animal
# * Cat is an Animal
# * Dogs bark
# * Cats meow
# * Cats have 9 lives 

# %% [md]
# ## Step 1 - Model Relationships
# * We would consider creating an Animal base class with two derived classes, Dog and Cat.  
# * Classes then form a heirarchical relationship.
# * Dog is an Animal
# * Cat is an Animal

# %% codecell
class Animal():
    pass

class Dog(Animal):
    """
    Dog is an Animal.
    """
    pass

class Cat(Animal):
    """
    Cat is an Animal
    """
    pass

# %% [md]
# ## Step 2 - Model Behaviors
# We define functions to model the sound behavior.  We place these functions
# in the class heirarchy based on our requirements.
# * Cats meow
# * Dogs bark
# * Note:  We'll build on this simple model over the next few notebooks 

# %% codecell
class Animal():
    pass

class Dog(Animal):
    def sound(self):
        """
        Dogs bark
        """
        return "Bark"

class Cat(Animal):
    def sound(self):
        """
        Cats meow
        """
        return "Meow"

# %% codecell
animal = Animal()

dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

# %% [md]
# ## Step 3 - Model State
# We use member variables to model state
# * Cats have 9 lives
# * Seems wrong for dogs not to have lives

# %% codecell
class Animal():
    pass

class Dog(Animal):
    def __init__(self):
        self.lives = 1
        
    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self):
        self.lives = 9

    def sound(self):
        return "Meow"

# %% codecell
cat = Cat()
print(f'Cat has {cat.lives} lives')

dog = Dog()
print(f'Dog has {dog.lives} lives')

# %% [md]
# # Inheritance Trees
# * No rule on how deep you can go with classes
# * For example:
#   * Working is a type of dog
#   * Hunting is a type of dog
#   * Lap is a type of dog

# %% codecell
class Animal():
    def __init__(self, lives=1):
        self.lives = lives

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        return "Bark"
    
class WorkingDog(Dog):
    pass

class HuntingDog(Dog):
    pass

class LapDog(Dog):
    pass

# %% codecell
pebbles = LapDog()
print(pebbles.sound())
print(pebbles.lives)


