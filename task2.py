import numpy as np

from rsdl.tensors import Tensor
from rsdl.layers import Linear

X = Tensor(np.random.randn(100, 3))
coef = Tensor(np.array([-7, +3, -9]).reshape(-1, 1))
y = X @ coef + 1

# TODO: define a linear layer
l = ...

# TODO: print weight and bias of linear layer

learning_rate = ...
batch_size = ...

for epoch in range(100):
    
    epoch_loss = 0.0
    
    for start in range(0, 100, batch_size):
        end = start + batch_size


        print(start, end)

        inputs = X[start:end]

        # TODO: predicted
        predicted = ...

        actual = y[start:end]
        # TODO: calcualte MSE loss
        w.zero_grad()
        b.zero_grad()
        
        # TODO: backward
        # hint you need to just do loss.backward()

        epoch_loss += ...


        # TODO: update w and b
        

# TODO: print weight and bias of linear layer
