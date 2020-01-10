# %% [md]
# # Scoping - Instance, Class & Static Methods

# %% [md]
# # Instance Methods
# * A method available to the instance
# * Has a reference to self
# * With a reference to self, it has access to the instance state

# %% codecell
class MyClass():
    def instanceWork(self):
        print('Instance Method - Work')

# %% codecell
my = MyClass()
my.instanceWork()

# %% [md]
# # Class Methods
# To attach a method to a class, use the @classmethod annotation and
# rather than self, use cls as the first parameter

# %% codecell
class MyClass():
    def instanceWork(self):
        print('Instance Method - Work')
        print(self)

    @classmethod
    def classWork(cls):
        print('Class Method - Work')
        print(cls)

# %% [md]
# You can call class methods using your reference to the class instance

# %% codecell
my = MyClass()
my.instanceWork()
my.classWork()

# %% [md]
# You can also call class methods using the class name

# %% codecell
MyClass.classWork()

# %% [md]
# # Usage : Alternative Constructors
# Class methods are great for creating alternative Constructors

# %% codecell
from datetime import date

# %% codecell
class Customer():
    def __init__(self, firstName:str, lastName:str, age:int):
        self.firstName = firstName
        self.lastName  = lastName
        self.age       = age

    def output(self):
        print(self.firstName, self.lastName, self.age)

    @classmethod
    def fromFullName(cls, fullName:str, age:int):
        firstName, lastName = fullName.split(' ')
        return cls(firstName, lastName, age)

# %% codecell
c1 = Customer('Anne', 'Smith', 30)
c2 = Customer.fromFullName('Cindy Williams', 50)

c1.output()
c2.output()

# %% [md]
# # Static Methods
# Convenient for grouping methods that logically make sense in a class
# but do not require an object.  Helper methods are good candidates for
# staticmethods in classes.

# %% codecell
class MyClass():
    def instanceWork(self):
        print('Instance Method - Work')
        print(self)

    @classmethod
    def classWork(cls):
        print('Class Method - Work')
        print(cls)

    @staticmethod
    def staticWork():
        print('Static Method - Work')

# %% codecell
c = MyClass()
c.staticWork()

# %% codecell
MyClass.staticWork()