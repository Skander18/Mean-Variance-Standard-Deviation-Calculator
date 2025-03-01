import numpy as np

def calculate(list):
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = (np.array(list, dtype=float).reshape((3,3)))
    
        # mean
    calculations['mean'].append(np.mean(matrix, axis=0, dtype=float).tolist())
    calculations['mean'].append(np.mean(matrix, axis=1, dtype=float).tolist())
    calculations['mean'].append(np.mean(list).tolist())

    # variance
    calculations['variance'].append(np.var(matrix, axis=0, dtype=float).tolist())
    calculations['variance'].append(np.var(matrix, axis=1, dtype=float).tolist())
    calculations['variance'].append(np.var(list).tolist())

    # standard deviation
    calculations['standard deviation'].append(np.std(matrix, axis=0, dtype=float).tolist())
    calculations['standard deviation'].append(np.std(matrix, axis=1, dtype=float).tolist())
    calculations['standard deviation'].append(np.std(list).tolist())
    
    # max
    calculations['max'].append(np.max(matrix, axis=0).tolist())
    calculations['max'].append(np.max(matrix, axis=1).tolist())
    calculations['max'].append(np.max(list).tolist())

    # min
    calculations['min'].append(np.min(matrix, axis=0).tolist())
    calculations['min'].append(np.min(matrix, axis=1).tolist())
    calculations['min'].append(np.min(list).tolist())
    
    # sum
    calculations['sum'].append(np.sum(matrix, axis=0, dtype=int).tolist())
    calculations['sum'].append(np.sum(matrix, axis=1, dtype=int).tolist())
    calculations['sum'].append(np.sum(list).tolist())




    return calculations


