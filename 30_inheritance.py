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
# * All Animals make a sound
# * Dogs bark
# * Cats meow
# * Cats have 9 lives

# %% [md]
# ## Step 1 - Model Relationships
# We would consider creating an Animal base class with two
# derived classes, Dog and Cat.  Classes then form a heirarchical relationship.

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
# * All Animals make a sound
# * Cats meow
# * Dogs bark

# %% codecell
class Animal():
    def sound(self):
        """
        All animals make a sound.  Each animal's sound is different.
        """
        return "Make Sound"

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
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

# %% [md]
# ## Step 3 - Model State
# We use member variables to model state
# * Cats have 9 lives

# %% codecell
class Animal():
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self):
        self.lives = 9

    def sound(self):
        return "Meow"

# %% codecell
cat = Cat()
print(cat.lives)

dog = Dog()
print(dog.lives)

# %% [md]
# # Rethinking Lives
# Rather than giving lives to cats we could improve this model.
# We'll use a constructor to help!
# * Implicitly Animals has one Life
# * Cats have 9 lives

# %% codecell
class Animal():
    def __init__(self, lives=1):
        self.lives = lives

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self):
        super().__init__(lives=9)

    def sound(self):
        return "Meow"

# %% codecell
cat = Cat()
print(cat.lives)

dog = Dog()
print(dog.lives)
