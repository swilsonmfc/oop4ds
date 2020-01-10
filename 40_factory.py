# %% [md]
# # Factory Pattern
# * Factory is a creational pattern
# * We use it when we want to control the construction & initialization of objects
# * In this example:
#   * We have a Reader that is "complicated"
#   * It has to read from different types of sources
#   * The sources may have different versions of the data
#   * We want to hide the complexity of setting up reading

# %% codecell
from abc import ABC
from abc import abstractmethod


# %% [md]
# # Data Loading Classes

# %% codecell 
class Loader(ABC):
    @abstractmethod
    def load(self):
        pass
    
    def read(self):
        pass
    
    def log(self, message):
        print(message)
        
class Version(ABC):
    @abstractmethod
    def map(self, d:dict):
        pass
    
class Reader():
    def __init__(self, loader:Loader, version:Version):
        self.loader = loader
        self.version = version
        
    def read(self):
        results = []
        self.loader.load()
        row = self.loader.read()
        while row is not None:
            mapped = self.version.map(row)
            results.append(mapped)
            row = self.loader.read()
        return results

# %% [md]
# There are three different ways to read in our data
# * CSV FlatFile
# * JSON
# * Database

# %% codecell
class CSVLoader(Loader):
    def load(self):
        self.log('Reading from CSV')
        
class JSONLoader(Loader):
    def load(self):
        self.log('Reading from JSON')
        
class DatabaseLoader(Loader):
    def load(self):
        self.log('Reading from Database')
        
# %% codecell
l = Loader()

# %% codecell
loaderCSV = CSVLoader()
loaderCSV.load()

loaderJSON = JSONLoader()
loaderJSON.load()

loaderDB = DatabaseLoader()
loaderDB.load()

# %% [md]
# There are two versions of data formats
# * V1
# * V2

# %% codecell
class DataVersion1():
    def map(self, d:dict):
        return (d['item'], d['customer'])

class DataVersion2():
    def map(self, d:dict):
        return (d['item'], d['customer'], d['quantity'])
    
# %% [md]
# # Creation Pattern
# What's the best way to pick the loader you need at runtime?

# %% [md]
# ## Main Method
# If we code a main method, we need to select the correct loader type
# and the correct version.  Our unittests around the main method
# would need to test all 6 paths in this example along with other duties in the main.

# %% [md]
# ## Factory Pattern

# %% codecell
class ReaderFactory():
    def getReader(self, config):
        loader = None
        if config['loader'] == 'CSV':
            loader = CSVLoader()
        if config['loader'] == 'JSON':
            loader = JSONLoader()
        if config['loader'] == 'DB':
            loader = DatabaseLoader()
            
        version = None
        if config['version'] == 1:
            version = DataVersion1()
        if config['version'] == 2:
            version = DataVersion2()
        
        return Reader(loader=loader, version=version)
    
# %% codecell
config = {'loader':'DB', 'version':2}
factory = ReaderFactory()
reader = factory.getReader(config)
reader.read()
