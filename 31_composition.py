# %% [md]
# # Overview
#
# We cover how to model relationships and behaviors in this class.
# * Is A  = Inheritance
# * Has A = Composition
#
# We model inheritance with classes and base classes.

# %% [md]
# # Example
# Requirements:
# * Albums have Songs
# * Albums have Artists
# * Bands have more than one artist
# * Bands, Artists, Songs, and Albums have Names
# * Albums are sold
# * Albums that sell 100,000 copies are Gold


# %% [md]
# ## Step 1 - Model Entities
# Tackle modeling the major actors in this system
# * Album
# * Song
# * Artist
# * Band

# %% codecell
class Album():
    pass

class Song():
    pass

class Artist():
    pass

class Band():
    pass

# %% [md]
# ## Step 2 - Model Compositions
# We assign variables to model compositions
# * Albums have Songs
# * Albums have Artists
# * Bands have Artists

# %% codecell
class Album():
    def __init__(self):
        self.songs = []
        self.artists = []

class Song():
    pass

class Artist():
    pass

class Band():
    def __init__(self):
        self.artists = []


