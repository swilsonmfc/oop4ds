# %% md
# # Singletons

# %% md
# # Dunder __new__

# %% codecell
class NotSingleton(object):
    pass

# %% codecell
ns1 = NotSingleton()
ns2 = NotSingleton()

print(ns1)
print(ns2)
print(ns1 == ns2)

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

# %% md
# # Tracking Handouts
# A trivial example of shared state

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
print(ts.handout())

ts2 = TrackingSingleton()
print(ts.handout())

print(ts1.handedOut())
print(ts2.handedOut())

    
# %% md
# # Allowable Creation


# %% md
# # Central Logging
