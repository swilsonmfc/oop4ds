# %% [md]
# # Introduction
# In this workbook we look at how to structure methods and the visibility they have.
# In particular, we'll look at scoping variables to our class and an instance of the class:
# * Class
# * Instance


# %% [md]
# # Class
# * Real world objects have state and behavior
# * Software objects have state and behavior
#   * State = variables
#   * Behavior = functions
# * In python we define a class as a template for objects we want to use
# * When we create a class, we create an instance of the class
# * Think "is a" for a class

# %% codecell
class A():
    pass

# %% codecell
a = A()

# %% [md]
# # State
# * State is represented by variables in a class

# %% codecell
class A():
    state = 'My State'

# %% codecell
a = A()
print(a.state)

# %% [md]
# # Behavior
# * Methods represent behavior in classes
   
# %% codecell
class A():
    def behavior(self, do):
        print('Doing', do)
        
# %% codecell
a = A()
a.behavior('Move')

# %% [md]
# # Self
# Reference to the object
# In some languages it is implied (java - this)
# In Python it's explicit declared in functions
# A method defined with self in a class is available 
# using the . followed by the function name.

# %% codecell
class A():
    def __init__(self, action):
        self.action = action
        
    def behavior(self):
        print('Doing', self.action)
        
# %% codecell
a1 = A('Run')
a1.behavior()

a2 = A('Walk')
a2.behavior()


# %% [md]
# # Why Classes
# * Modularity - Modular classes allow you to define in one place independent of other objects
# * Code Re-Use - Share the implementation within and between projects
# * Manage Complexity - Classes model real world objects and improve readability / understanding
# * Debugging - Hiding information in classes makes debugging easier 