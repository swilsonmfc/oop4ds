# %% [md]
# # Singletons
# With a singleton, we want exactly one instance of a class created
# This is typically done so we can manage state in a centralized location
# An example would of a singleton, may be a logger that manages writing
# to one or more files.  We want to use the logger from many places and 
# it's convenient to create an instance of a logger as needed, but implementation-wise
# we want to logger to be the same instance so we can safely write to the file. 

# %% codecell
class NotSingleton(object):
    pass

# %% codecell
ns1 = NotSingleton()
ns2 = NotSingleton()

print(ns1)
print(ns2)
print(ns1 == ns2)
print(ns1 is ns2)

# %% [md]
# # Dunder __new__
# The key to creating a singleton, is intercepting the dunder __new__ method.
# This is called when we want to construct an instance.  If you look at the 
# signature, it's a class method.  Within the method, we look to see if 
# an instance of our class exists.  If it does, we return that instance. If it
# does not, we create an instance of the class, save it in our Singleton class
# and return the instance.

# %% codecell
class Singleton(object):
    _instance = None  
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

# %% codecell
s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)
print(s1 == s2)

# %% [md]
# # Tracking Handouts
# A toy example of shared state using a Singleton.  Our need is to track the number of times
# we hand out a reference.  Note:  we need to take special care of our singleton initialization.

# %% codecell
class TrackingSingleton(object):
    _instance = None
    _handouts = 0
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def handout(self):
        TrackingSingleton._handouts += 1
        return TrackingSingleton._handouts
    
    def handedOut(self):
        return TrackingSingleton._handouts

# %% codecell
ts1 = TrackingSingleton()
print(ts1.handout())

ts2 = TrackingSingleton()
print(ts2.handout())

print(ts1.handedOut())
print(ts2.handedOut())

    
# %% [md]
# # Enforcing Maximum Handouts
# We have state in our instance class that we need to run exactly once

# %% codecell
class MaxHandoutSingleton(object):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            
            # Setup our instance state on max handouts & current handouts
            cls._instance._handouts = 0
            cls._instance._max = 3
        
        return cls._instance
    
    def __init__(self):
        # Runs on every construction
        pass
    
    def handout(self):
        if self._handouts == self._max:
            raise Exception('Max Handouts Reached')
        self._handouts += 1
        return self._handouts
    
    def turnin(self):
        self._handouts -= 1
    
    def handedOut(self):
        return self._handouts

# %% codecell
maxer = MaxHandoutSingleton()  
maxer.handout(); print(maxer.handedOut())
maxer.handout(); print(maxer.handedOut())
maxer.handout(); print(maxer.handedOut())
maxer.handout()

# %% codecell
maxer.turnin()
maxer.turnin()
print(maxer.handedOut())
    
# %% [md]
# # Singleton Factory
# It's common to make our singleton the basis of a Factory pattern

# %% codecell
class LimitedResource():
    def __init__(self, id):
        self._id = id
        
    def __enter__(self):
        print(' Entering')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(' Exiting')
        factory = LimitedResourceFactory()
        factory.returnItem(self)
        

class LimitedResourceFactory(object):
    _instance = None
        
    def __new__(cls, *args, **kwargs): 
        print('New')
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """
        Create items in a pool of resources
        """
        if self._initialized == False:
            print('Init')
            self.pool = []
            self.out  = []       
            for x in range(3):
                self.pool.append(LimitedResource(x))
            self._initialized = True
        
    
    def checkoutItem(self):
        """
        Take an item from the pool or exception if not available
        """
        if len(self.pool) == 0:
            raise('No Resources Available')
        item = self.pool.pop()
        self.out.append(item)
        print(f'Handing out item {item._id}')
        return item
    
    def returnItem(self, item):
        """
        Returns to the pool
        (Note, not checking edge cases, like called twice etc)
        """
        print(f'Item {item._id} returned to pool')
        self.out.remove(item)
        self.pool.append(item)
        
    def status(self):
        print('Pool Status')
        for i in self.pool:
            print(f' Item {i._id} in pool')
        for i in self.out:
            print(f' Item {i._id} handed out')

# %% codecell
with LimitedResourceFactory().checkoutItem() as item:
    print('  Doing some work!!!')
    LimitedResourceFactory().status()
    
print('After Complete')
LimitedResourceFactory().status()

# %% codecell
item = LimitedResourceFactory().checkoutItem()
print('Doing more work!!!')
LimitedResourceFactory().status()
print('Returning Item')
LimitedResourceFactory().returnItem(item)
LimitedResourceFactory().status()