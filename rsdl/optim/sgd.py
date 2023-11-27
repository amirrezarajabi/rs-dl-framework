from optim import Optimizer

# TODO: implement step function
class SGD(Optimizer):
    def __init__(self, layers, learning_rate=0.1):
        super().__init__(layers)
        self.learning_rate = learning_rate

    def step(self):
        for l in self.layers:
            l.weight = ...
            if l.need_bias:
                l.bias = ...