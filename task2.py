import numpy as np

from rsdl import Tensor


X = Tensor(np.random.randn(100, 3))
coef = Tensor(np.array([-7, +3, -9]).reshape(-1, 1))
y = X @ coef + 1
y = y + Tensor(np.random.randn(100, 1) * 0.01)

# TODO: define a linear layer and optimizer
l = ...

# TODO: print weight and bias of linear layer


# TODO: init optimizer and loss function

learning_rate = ...
batch_size = ...

losses = []

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
        
        # TODO: backward
        # hint you need to just do loss.backward()


        # TODO: add loss to epoch_loss
        epoch_loss += ...


        # TODO: update w and b
        
    epoch_loss = epoch_loss / (100 // batch_size)
    losses.append(epoch_loss)

# TODO: print weight and bias of linear layer

# TODO: plot the loss 