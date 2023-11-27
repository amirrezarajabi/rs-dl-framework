from tensors import Tensor

def Sigmoid(t: Tensor) -> Tensor:
    return 1.0/(1.0+((-t).exp()))

def Tanh(t: Tensor) -> Tensor:
    return (t.exp()-(-t).exp())/(t.exp()+(-t).exp())

def Relu(t: Tensor) -> Tensor:
    data=np.maximum(0,tensor.data)
    req_grad=t.requires_grad
    if req_grad:
        def grad_fn(grad: np.ndarray):
            return grad * np.where(t.data>=0 , 1 , 0)
        
        depends_on = [Dependency(t, grad_fn)]
    else:
        depends_on = []
    return Tensor(data=data, requires_grad=req_grad, depends_on=depends_on)


def LeakyRelu(t: Tensor,leak=0.05) -> Tensor:
    """
    fill 'data' and 'req_grad' and implement LeakyRelu grad_fn 
    hint: use np.where like Relu method but for LeakyRelu
    """
    # TODO
    data=...
    req_grad=...
    if req_grad:
        def grad_fn(grad: np.ndarray):
            return None
        
        depends_on = [Dependency(t, grad_fn)]
    else:
        depends_on = []

    return Tensor(data=data, requires_grad=req_grad, depends_on=depends_on)


