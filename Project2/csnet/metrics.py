import numpy as np


def accuracy(true: np.ndarray, pred: np.ndarray) -> int:
    """
    Calculates accuracy of classification
    """

    if pred.shape[0] != true.shape[0]:
        raise AttributeError(
            f"Wrong shape of true and pred: {pred.shape} != {true.shape}"
        )
    true = true.reshape(-1,1)

    return np.sum(pred == true) / pred.shape[0]
