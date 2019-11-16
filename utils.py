import numpy as np

def dataSplit(arr, N):
    split = np.split(arr, np.arange(N, arr.shape[0], N), axis=0)
    split.pop().shape
    split = np.stack(split)

    split = np.split(split, np.arange(N, arr.shape[-1], N), axis=-1)
    split.pop().shape
    split = np.stack(split)

    return split.reshape(-1, N, N, 1)