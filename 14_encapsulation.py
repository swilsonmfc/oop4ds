# %% [md]
# # Encapsulation
# * Bundling of data with the methods that operate on that data
# * Restricting direct access to some of an object's components

# %% [md]
# # Protected Methods
# Use a single underscore to indicate that the method is not part of your API
# and it should be treated as private.  Note, the compiler and interpreter do
# not enforce this.  It's on the users of an API to respect protected members.

# %% codecell
class Base():
    def public_method(self):
        print('public')

    def _protected_method(self):
        print('protected')

# %% codecell
b = Base()
b.public_method()
b._protected_method()

# %% [md]
# # Private Methods
# Private methods are not accessible outside of the class

# %% codecell
class Base():
    def public_method(self):
        print('public')

    def __private_method(self):
        print('private')

class Derived(Base):
    pass

# %% codecell
b = Base()
b.public_method()
b.__private_method()

# %% [md]
# # Private Methods and Derived Classes
# Private methods are not accessible outside of the class

# %% codecell
d = Derived()
d.public_method()
d.__private_method()

# # Private Methods Within Class
# Private
# %% codecell
class Base():
    def public_method(self):
        print('public')

    def __private_method(self):
        print('private')

    def access_method(self):
        self.__private_method()

class Derived(Base):
    pass

# %% codecell
b = Base()
b.public_method()
b.access_method()

d = Derived()
d.public_method()
d.access_method()

# %% [md]
# # Protected Member Variables

# %% codecell
class ProtectedVariables():
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName  = lastName

# %% codecell
p = ProtectedVariables('First', 'Last')
print(p._firstName)
print(p._lastName)

# %% [md]
# # Private Member Variables

# %% codecell
class PrivateVariables():
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName  = lastName

# %% codecell
p = PrivateVariables('First', 'Last')
print(p.__firstName)
