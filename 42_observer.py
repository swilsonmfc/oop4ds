# %% [md]
# # Observer Problem
# How can we watch for state changes and events in a manner that allows
# us to extend and test our code without making a codebase woven with
# orthogonal concerns. 

# %% codecell  
import numpy as np
class NeuralNetwork():
    def forward(self, batch):
        """
        Forward pass through the network
        Returns our prediction (output)
        """
        print('Forward Pass')
    
    def backward(self, loss):
        """
        Backward pass through the network
        Returns our gradients given the loss
        """
        print('Backward Pass')
        
    
    def computeLoss(self, preds):
        """
        Compute our loss between pred / actual
        """
        print('Compute Loss')
    
    def updateWeights(self, gradients, learning_rate=0.001):
        """
        Given the gradients and our learning rate, update our weights
        """
        print('Update Weight Parameters')
    
    def train(self, epochs, batches):
        """
        Training loop, for each epoch, for each batch

        """
        for epoch in epochs:
            for batch in batches():
                preds = self.forward(batch)
                loss  = self.computeLoss(preds)
                gradients = self.backward(loss)
                self.updateWeights(gradients)

# %% [md]
# # Extend Functionality
# In this example, we want to do three things:
# * Adjust learning rate schedule (annealling)                
# * Log loss after each batch
# * Log accuracy after each epoch
# We're also quite sure we'll want to make more adjustments


# %% [md]
# # Observer Pattern
# * Rather than add orthoginal code into our net, we separate concerns
# * Observed -> Code that creates events / state changes (our neural network)
# * Observer -> Watches for changes and dispatches events to those who are interested
# * Callback -> The interface an iterested party implements to get notified 
# Note:  Our code focuses on a specific implementation, and takes advantage of dunders
# for implementation details. We don't fully implement a neural net as well
# preferring to focus on the details of the three actors in this pattern.
                
# %% codecell  
class Callback():
    """
    Marker Interface
    """
    pass  
    
class Observer():
    def __init__(self):
        """
        Create a list of callbacks
        """
        self.callbacks = []
        
    def registerCallback(self, callback):
        """
        Add the callback to our list
        """
        self.callbacks.append(callback)

    def __call__(self, *args, **kwargs):
        """
        Got an event, invoke on our callbacks given the name
        """
        invoke = args[0]
        for c in self.callbacks:
            try:
                func = getattr(c, invoke)
                func(args[1])
            except:
                pass
        
# %% [md]
# # Network 2.0
        
# %% codecell
class NeuralNetwork():
    def __init__(self, callbacks=None):
        """
        Setup an observer and add the callbacks provided
        """
        self.observer = Observer()
        if callbacks is not None:
            for c in callbacks:
                self.observer.registerCallback(c) 
                
    def observe(self, action, state={}):
        """
        Observed a state or event, propagate to observer to forward
        Set a reference to this neural network
        """
        state['net'] = self
        self.observer(action, state)
        
    def forward(self, batch):
        """
        Forward pass through the network
        Returns our prediction (output)
        """
        print('Forward Pass')
    
    def backward(self, loss):
        """
        Backward pass through the network
        Returns our gradients given the loss
        """
        print('Backward Pass')
          
    def computeLoss(self, preds):
        """
        Compute our loss between pred / actual
        """
        print('Compute Loss')
        return np.random.random()
        
    def computeAccuracy(self):
        """
        Compute our loss between pred / actual
        """
        print('Compute Accuracy')
        return np.random.random()
    
    def updateWeights(self, gradients, learning_rate=0.001):
        """
        Given the gradients and our learning rate, update our weights
        """
        print('Update Weight Parameters')
    
    def train(self, epochs, batches, learning_rate=0.001):
        """
        Training loop, for each epoch, for each batch

        """
        state = {}
        state['epochs']  = epochs
        state['batches'] = batches
        state['learning_rate'] = learning_rate
        
        for epoch in range(epochs):
            state['epoch'] = epoch
            self.observe('beforeEpoch', state)
            
            for batch in range(batches):
                state['batch'] = batch
                self.observe('beforeBatch', state)
                
                preds = self.forward(batch)
                loss  = self.computeLoss(preds)
                gradients = self.backward(loss)
                self.updateWeights(gradients)
                
                state['loss'] = loss
                self.observe('afterBatch', state)
                
            accuracy = self.computeAccuracy()
            state['accuracy'] = accuracy                
            self.observe('afterEpoch', state)

# %% [md]
# # Logging
            
# %% codecell
class CallbackLogging(Callback):
    def beforeEpoch(self, state):
        print(f'-> Before Epoch {state["epoch"] + 1} of {state["epochs"]}')
    
    def afterEpoch(self, state):
        print(f'-> After Epoch {state["epoch"] + 1} of {state["epochs"]}\n')
    
    def beforeBatch(self, state):
        print(f'--> Before Batch {state["batch"] + 1} of {state["batches"]}')
    
    def afterBatch(self, state):
        print(f'--> After Batch {state["batch"] + 1} of {state["batches"]}')
  
    
# %% codecell
logger   = CallbackLogging()
ann = NeuralNetwork(callbacks=[logger])
ann.train(2,2)

# %% [md]
# # Callback Loss & Accuracy Tracking 

# %% codecell
class CallbackMetricTracker(Callback):
    def __init__(self):
        self.losses = []
        self.accuracy = []
        
    def afterBatch(self, state):
        self.losses.append(state['loss'])
        
    def afterEpoch(self, state):
        self.accuracy.append(state['accuracy'])
        
    def __str__(self):
        return(f'Losses {self.losses}\nAccuracy {self.accuracy}')
        
# %% codecell
logger   = CallbackLogging()
tracker  = CallbackMetricTracker()
ann = NeuralNetwork(callbacks=[logger, tracker])
ann.train(2,2)     
print(tracker)

# %% [md]
# # Callback Learning Rate Annealing
# Most modern frameworks (PyTorch, Keras, TF), hold the learning rate with the optimizer.
# In this simple net, we're building our network and optimizer in one class.

# %% codecell
class CallbackLearningRate(Callback):    
    def afterBatch(self, state):
        """
        Log a message for demo
        """
        print(f'. Anneal learning rate {state["learning_rate"]}')
                
# %% codecell
logger   = CallbackLogging()
tracker  = CallbackMetricTracker()
learning = CallbackLearningRate()
ann = NeuralNetwork(callbacks=[logger, tracker, learning])
ann.train(2,2)     
print(tracker)