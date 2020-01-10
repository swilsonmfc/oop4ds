# %% [md]
# # State Pattern
# * How can we enforce viable transitions without heavy use of if statements?

# %% codecell
class FlightState():
    name = 'State'
    allowed = []

    def switch(self, switchTo):
       """ Switch to new state """
       if switchTo.name in self.allowed:
          print(f'Current: {self.name} => switched to new state {switchTo.name}')
          self.__class__ = switchTo
       else:
          print(f'Current: {self.name} => switching to {switchTo} not possible.')
    
    def __str__(self):
       return self.name
   
    def __repr__(self):
        return self.name
  
# %% codecell
class AtGate(FlightState):    
    name = 'AtGate'
    allowed = ['Taxiing']
        
class Taxiing(FlightState):
    name = 'Taxiing'
    allowed = ['AtGate', 'Holding', 'Airborne']
    
class Airborne(FlightState):
    name = 'Airborne'
    allowed = ['Climbing']
    
class Climbing(FlightState):
    name = 'Climbing'
    allowed = ['Cruising', 'Descending']
    
class Cruising(FlightState):
    name = 'Cruising'
    allowed = ['Climbing', 'Descending']
    
class Descending(FlightState):
    name = 'Descending'
    allowed = ['Landing']
    
class Landing(FlightState):
    name = 'Landing'
    allowed = ['Taxiing']
    
class Holding(FlightState):
    name = 'Holding'
    allowed = ['Taxiing']
    
# %% codecell
class Flight():
    def __init__(self, state=AtGate()):
        self._state = state
        self._history = [state]
    
    def change(self, state):
      """ Change state """
      self._state.switch(state)
      self._history.append(state)
      
    def history(self):
        for i in self._history:
            print(i.name)
      

# %% codecell
flight75 = Flight()
flight75.change(Taxiing)
flight75.change(Holding)
flight75.change(Taxiing)
flight75.change(Airborne)
flight75.change(Climbing)
flight75.change(Cruising)
flight75.change(Descending)
flight75.change(Landing)
flight75.change(Taxiing)
flight75.change(AtGate)

# %% codecell
flight75.history()