<<<<<<< HEAD
import numpy as np

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
=======
import numpy as np

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
>>>>>>> 1a219d094641248cc7d18636d44bae02ec4c8783
        return train, test