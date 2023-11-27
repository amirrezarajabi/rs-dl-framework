from optim.sgd import SGD
from optim.adam import Adam
from optim.rmsprop import RMSprop
from optim.momentum import Momentum

class Optimizer:
    def __init__(self, layers):
        self.layers = layers
    
    def zero_grad(self):
        for l in self.layers:
            l.zero_grad()