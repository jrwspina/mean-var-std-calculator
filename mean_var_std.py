import numpy as np

KEYS = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

def calculate(list):
    if(len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.array(list).reshape((3,3))
    calculations = {key: [] for key in KEYS}

    for i in range(2):
        calculations['mean'].append(np.mean(matrix, axis=i).tolist())
        calculations['variance'].append(np.var(matrix, axis=i).tolist())
        calculations['standard deviation'].append(np.std(matrix, axis=i).tolist())
        calculations['max'].append(np.max(matrix, axis=i).tolist())
        calculations['min'].append(np.min(matrix, axis=i).tolist())
        calculations['sum'].append(np.sum(matrix, axis=i).tolist())
        
    calculations['mean'].append(np.mean(matrix))
    calculations['variance'].append(np.var(matrix))
    calculations['standard deviation'].append(np.std(matrix))
    calculations['max'].append(np.max(matrix))
    calculations['min'].append(np.min(matrix))
    calculations['sum'].append(np.sum(matrix))
    
    return calculations