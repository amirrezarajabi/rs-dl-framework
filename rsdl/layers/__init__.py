import numpy as np

from layers.fully_connected import Linear

def xavier_initializer(shape):
    return np.random.randn(*shape) * np.sqrt(1/shape[0])

def he_initializer(shape):
    return np.random.randn(*shape) * np.sqrt(2/shape[0])

def zero_initializer(shape):
    return np.zeros(shape)

def one_initializer(shape):
    return np.ones(shape)

def initializer(shape, mode="xavier"):
    if mode == "xavier":
        return xavier_initializer(shape)
    elif mode == "he":
        return he_initializer(shape)
    elif mode == "zero":
        return zero_initializer(shape)
    elif mode == "one":
        return one_initializer(shape)
    else:
        raise NotImplementedError("Not implemented initializer method")