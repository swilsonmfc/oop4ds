# %% [md]
# # Property
# Properties are a clean way of hiding internal details in a convenient API friendly way

# %% [md]
# # Simple Approach
# * As a user of the class, can I change it?
# * What happens if I do?
# * Are there any rules about changing it?
# * The simple approach lacks expressiveness

# %% codecell
class Person():
    name = 'my name'

# %% [md]
# # Functional Get / Set
# * I know more about this with functions fronting the variable
# * I know I can't direcltly access it (double underscore performs a rewrite)
# * The method gives me an opportunity to inject any business logic I need
    
# %% codecell
class Person():
    def __init__(self):
        self.__name = None
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
# %% codecell
p = Person()
print(p.getName())

p.setName('Tom')
print(p.getName())
    

# %% [md]
# # Property
# * Properties sit atop a method
# * The getter method has the @property annotation & uses the method name
# * If the property can be written to, we add an annotation @[name].setter
# * Properties do not have to be aligned to one variable

# %% codecell
class Person():
    def __init__(self):
        self.__firstName = None
        self.__lastName  = None
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, value):
        self.__firstName = value
        
    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, value):
        self.__lastName = value
        
    @property 
    def fullName(self):
        return self.__firstName + " " + self.__lastName
    
        
# %% codecell
p = Person()
print(p.firstName)

p.firstName = 'Tom'
print(p.firstName)

p.lastName = 'Thumb'
print(p.lastName)

# Property for full name
print(p.fullName)

# %% codecell
#Can't set - not defined
p.fullName = 'Tom T'

# %% codecell
# Can't get the state directly
print(p.__firstName)