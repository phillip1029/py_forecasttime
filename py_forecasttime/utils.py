import pandas as pd 
import numpy as np

# Time Series dataframe transform to the format ready for machine learning and deep learning.
# Time related feature creation
# time series data standardization
# time series data decomposition
 
# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = [], []
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

# divide training and testing, default as 70:30
def divideTrainTest(dataset, test=0.3):
    
    if test < 1:
        test_size = int(len(dataset) * test)
        train_size = len(dataset) - test_size
        train, test = dataset[0:train_size], dataset[train_size:]
        return train, test
    if test > 1:
        test_size = test
        train_size = len(dataset) - test_size
        train, test = dataset[0:train_size], dataset[train_size:]
        return train, test

