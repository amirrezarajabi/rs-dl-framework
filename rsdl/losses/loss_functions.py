from tensors import Tensor

def CategoricalCrossEntropy(preds: Tensor, actual: Tensor):
    loss=0
    loss-= actual*preds.log().sum()
    return loss

def MeanSquaredError(preds: Tensor, actual: Tensor):
    # TODO 
    return None