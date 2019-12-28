# %% md
# # Dunders
# In addition to constructors and initialization (__init__)
# Dunders control several aspects of objects.
# * str  = familiar output from print
# * repr = debugging and formal representation

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
       self.x = x
       self.y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self.x, self.y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self.x, self.y)


# %% codecell
# Examples
p = Point(10, 20)

# str / print
print(str(p))  # Same as "print t"
print(p)

# repr
print(repr(p))

# %% md
# # Arithmetic Dunders
# Special dunders implement arithmetic operations + - * /
# * Plus : __add__
# * Subtract : __sub__
# * Multiply : __mul__
# * Divide : __div__

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
       self.x = x
       self.y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self.x, self.y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self.x, self.y)

    # Adding Points
    def __add__(self, obj):
        return (self.x + obj.x, self.y + obj.y)

# %% codecell
p1 = Point(5, 5)
p2 = Point(10, 10)
p1 + p2

# %% md
# # Equality Dunder
# Special dunder for comparison of equals
# * Equals : __eq__
# * Less Than : __lt__
# * Greater Than : __gt__

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
       self.x = x
       self.y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self.x, self.y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self.x, self.y)

    # Adding Points
    def __add__(self, obj):
        return (self.x + obj.x, self.y + obj.y)

    # Equals
    def __eq__(self, obj):
        if (self.x == obj.x and self.y == obj.y):
            return True
        return False

# %% codecell
p1 = Point(5, 5)
p2 = Point(5, 10)
p3 = Point(10, 5)
p4 = Point(5, 5)

# %% codecell
p1 == p2
p1 == p3
p1 == p4

# %% md
# # Hash
# Defines the hash key a dictionary uses
# If you derive from Object, you will inherit the __hash__ implementation
# If you don't derive from Object, you have to implement __hash__
# Rules for hash:
# * Hash must never change through the lifetime of an object
# * Classes are unhashable if you implement __eq__ but not __hash__
# * Hash does not mean equality.  There can be collisions.
# * Consider using the hash function to hash an immuatable type (pass a tuple)

# %% codecell
d = {}
p1 = Point(5, 5)
d[p1] = 'Treasure'

class PointFromObject(object):
    pass

# %% codecell
d = {}
p = PointFromObject()
d[p] = 'Treasure'
d

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self._x, self._y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self._x, self._y)

    # Adding Points
    def __add__(self, obj):
        return (self._x + obj._x, self._y + obj._y)

    # Equals
    def __eq__(self, obj):
        if (self._x == obj._x and self._y == obj._y):
            return True
        return False

    # hash - a trivial example
    # We're using mutable values to define a hash, not a good plan
    # So, we've flagged our x and y with an underscore to indicate protected
    def __hash__(self):
        return hash((self._x, self._y))


# %% codecell
d = {}
d[Point(5, 5)]   = 'Treasure'
d[Point(3, 3)]   = 'Trap'
d[Point(10, 10)] = 'Ship'
d

# %% md
# # With Block -- Context Managers
# * The with block interacts with two dunders
# * Entering a with block calls __enter__
# * Exiting a with block calls __exit__
# * You often see this around a file resource
# * with open(file) as f: ...
# * We use this dunder to handle resource clean up automatically

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self._x, self._y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self._x, self._y)

    # Adding Points
    def __add__(self, obj):
        return (self._x + obj._x, self._y + obj._y)

    # Equals
    def __eq__(self, obj):
        if (self._x == obj._x and self._y == obj._y):
            return True
        return False

    # Hash
    def __hash__(self):
        return hash((self._x, self._y))
    
    # With Support
    def __enter__(self):
        print('Entering')
        
    # exc_type - Exception Type
    # exc_val  - Exception Value
    # exc_tb   - Exception Traceback
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting')

# %% codecell
with (Point(3, 3)) as pt:
    print('Using our Point')

# %% md
# # Call

# %% codecell
class Point:

    # Constructor
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Called by repr(). Object information
    def __repr__(self):
       return 'Point (%s, %s)' % (self._x, self._y)

    # Called by str(). Readable formatting
    def __str__(self):
       return '(%s, %s)' % (self._x, self._y)

    # Adding Points
    def __add__(self, obj):
        return (self._x + obj._x, self._y + obj._y)

    # Equals
    def __eq__(self, obj):
        if (self._x == obj._x and self._y == obj._y):
            return True
        return False

    # Hash
    def __hash__(self):
        return hash((self._x, self._y))
    
    # With Support
    def __enter__(self):
        print('Entering')
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting')
    
    # Call
    def __call__(self, val):
        if val == 'X' or val == 'x':
            return self._x
        if val == 'Y' or val == 'y':
            return self._y


# %% codecell
c = Point(5,6)
print(c('X'))
print(c('Y'))