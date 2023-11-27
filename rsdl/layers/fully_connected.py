from tensors import Tensor
from layers import initializer

class Linear:

    def __init__(self, in_channels, out_channels, need_bias=True, mode='xavier') -> None:
        # set input and output shape of layer
        self.shape = (in_channels, out_channels)
        self.need_bias = need_bias
        self._weight = Tensor(
            data=initializer(self.shape, mode=mode),
            requires_grad=True
        )
        self._bias = Tensor(
            data=initializer((self.shape[1]), mode="zero"),
            requires_grad=need_bias,
        )

    def forward(self, inp):
        return (inp @ self._weight) + self._bias
    
    def parameters(self):
        yield self._weight
        if self.need_bias:
            yield self._bias