# %% [md]
# # Constructors
# When we construct an object we initialize our class
# with the dunder init (__init__) method. 

# %% codecell
class Example():
    def __init__(self):
        print('Running init')
        self.some_variable = 1

# %% codecell
e = Example()
print(f'Value {e.some_variable}')

# %% [md]
# # Constructors & Inheritance
# If you don't initiatlize your base class it's
# dunder init will not run.  Any initialization
# that would occur there does not run.

# %% codecell
class Example():
    def __init__(self):
        print('Running Example Init')
        self.example_variable = 1

class Derived(Example):
    def __init__(self):
        print('Running Derived Init')
        self.derived_variable = 2

# %% codecell
d = Derived()
print(f'Example Variable {d.example_variable}')
print(f'Derived Variable {d.derived_variable}')

# %% [md]
# # Super
# You can initialize your base class with a call to super().__init__()

# %% codecell
class Example():
    def __init__(self):
        print('Running Example Init')
        self.example_variable = 1

class Derived(Example):
    def __init__(self):
        super().__init__()
        print('Running Derived Init')
        self.derived_variable = 2

# %% codecell
d = Derived()
print(f'Example Variable {d.example_variable}')
print(f'Derived Variable {d.derived_variable}')

# %% [md]
# # Super
# You can pass parameters as defined in __init__ to super's dunder init (constructor)

# %% codecell
class Example():
    def __init__(self, value):
        print('Running Example Init')
        self.example_variable = value

class Derived(Example):
    def __init__(self, value):
        super().__init__(value ** 2)
        print('Running Derived Init')
        self.derived_variable = value
        
# %% codecell
d = Derived(4)
print(f'Example Variable {d.example_variable}')
print(f'Derived Variable {d.derived_variable}')

# %% [md]
# # Recall Aminals, Dogs & Cats

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

# %% [md]
# # Refactor Aminals, Dogs & Cats
# We want to push the definition of lives into our base class since it 
# pertains to both cats and dogs (and presumably any animal)


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

# %% codecell
animal = Animal()
print(animal.lives)

dog = Dog()
print(dog.lives)

cat = Cat()
print(cat.lives)