# %% md
# # Inheritance
# In this inheritance example we want to design a set of functionality.
# To accomplish that we'll build some classes that will
# be remniscent of sklearn.
#
# Our requirements:
# * Transformations are fit to data
# * Transformations transform data
# * Normalizing data is a transformation
# * Models are fit to data
# * Fitted Models predict given data
# * Linear is a type of Model
# * Logistic is a type of Model
# * PCA is a Transformations
# * PCA is a Model
# * Pipelines are a serial list of Transforms or Models

# %% md
# # Learning Objects Fit

# %% codecell
class Base():
    """
    A Base class models functionality that can learn from data.
    We use a fit method to handle learning.
    """
    def __init__(self):
        pass

    def fit(self, X, y):
        pass

# %% md
# # Transforms

# %% codecell
class BaseTransform(Base):
    """
    The BaseTransform method performs a transformation of data.
    It can learn parameters it needs from data.
    It derives from Base, giving it a fit method.
    """
    def __init__(self):
        pass

    def transform(self, X):
        pass

class Normalize(BaseTransform):
    def __init__(self):
        pass

    def fit(self, X, y):
        print('Fit Normalize')

    def transform(self, X):
        print('Transform Normalize')

# %% md
# # Models

# %% codecell
class BaseModel(Base):
    """
    Our BaseModel learns from data and can make a prediction given new data.
    It derives from Base giving it a fit method.
    """
    def __init__(self):
        pass

    def predict(self, X):
        pass

class LinearModel(BaseModel):
    def __init__(self):
        super().__init__()

    def fit(self, X, y):
        print('Fit Linear Model')

    def predict(self, X):
        print('Predict Linear Model')

class LogisticModel(BaseModel):
    def __init__(self):
        super().__init__()

    def fit(self, X, y):
        print('Fit Logistic Model')

    def predict(self, X):
        print('Predict Logistic Model')

# %% md
# # Models that Transform

# %% codecell
class PCA(BaseModel, BaseTransform):
    def __init__(self):
        pass

    def fit(self, X, y):
        print('Fit PCA')

    def transform(self, X):
        print('Transform PCA')

    def predict(self, X):
        print('Predict PCA')

# %% md
# # Pipelines are Compositions

# %% codecell
class Pipeline(Base):
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def fit(self, X, y):
        for obj in self.steps:
            if isinstance(obj, Base):
                obj.fit(X, y)

    def transform(self, X):
        for obj in self.steps:
            if isinstance(obj, BaseTransform):
                obj.transform(X)

    def predict(self, X):
        for obj in self.steps:
            if isinstance(obj, BaseModel):
                obj.predict(X)

# %% md
# Running a Pipeline

# %% codecell
X = []
y = []
pipe = Pipeline()
pipe.add(Normalize())
pipe.add(PCA())
pipe.add(LinearModel())
pipe.fit(X, y)
pipe.predict(X)
pipe.transform(X)
