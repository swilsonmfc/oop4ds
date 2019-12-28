# %% md
# # Introduction
# In this workbook we look at how to structure methods and the visibility they have.
# In particular, we'll look at scoping variables to our class and an instance of the class:
# * Class
# * Instance


# %% md
# # Defining a Class
# Defining a class

# %% codecell
class A():
    pass

# %% md
# # Self
# Reference to the object
# In some languages it is implied (java - this)
# In Python it's explicit declared in functions
# A method defined with self in a class is available 
# using the . followed by the function name.
    
# %% codecell
class A():
    def behavior(self, do):
        print('Doing', do)
        
# %% codecell
a = A()
a.behavior('Move')

# %% md
# # Defining a Derived Class
# Example of fefining a base and derived class
# In this example, class B derives from A
# In other words, B is an A

# %% codecell
class A():
    pass

class B(A):
    pass

# %% md
# # Inheritance and Methods
# Methods are inherited in base classes
# In this example, talk is defined in A and is
# inherited to all subclasses including B.

# %% codecell
class A():
    def talk(self):
        print('Hello')

class B(A):
    pass

# %% codecell
b = B()
b.talk()

# %% md
# # Inheritance and Overriding
# Methods can be overridden by a subclass.
# In this example, talk is defined in A and is
# inherited to all subclasses including B & C.
# C has a different implementation of talk.
# We say that C overrides talk.

# %% codecell
class A():
    def talk(self):
        print('Hello')

class B(A):
    pass

class C(A):
    def talk(self):
        print('Goodbye')

# %% codecell
b = B()
b.talk()

c = C()
c.talk()
