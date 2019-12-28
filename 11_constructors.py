# %% md
# # Dunder methods
# Start with a double underscore

# %% md
# # Constructors
# There are two methods invoked when you create an object.
# * __new__ 
# * __init__
# New creates an object in memory and init gives you an opportunity to initiatize
# The object before handing it to a client.  It is relatively uncommon to override
# New, but there are some patterns that can take advantage of this 2 method contruction.


# %% codecell
class Example():
    def __init__(self):
        print('Running init')
        self.some_variable = 1

# %% codecell
e = Example()
print(f'Value {e.some_variable}')

# %% md
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

# %% md
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
