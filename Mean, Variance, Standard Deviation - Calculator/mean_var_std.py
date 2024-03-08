import numpy as np
import sys

def calculate(list_of_values):

    solution = {}

    if len(list_of_values) < 9:
        raise ValueError("List must contain nine numbers.")

    # Transformando a list em um numpy array
    array = np.array(list_of_values)

    # Transformando o numpy array em uma matriz 3x3 (numpy array 3x3)
    matrix = np.array([ array[0:3], array[3:6], array[6:9] ], dtype=object)

    # Mean
    axis1_mean = list(matrix.mean(axis=0))
    axis2_mean = list(matrix.mean(axis=1))
    flattened_mean = matrix.mean()

    # Variance
    axis1_var = list(np.var(matrix, axis=0))
    axis2_var = list(np.var(matrix, axis=1))
    flattened_var = np.var(matrix)

    # std
    axis1_std = list(matrix.std(axis=0, dtype=float))
    axis2_std = list(matrix.std(axis=1, dtype=float))
    flattened_std = matrix.std()

    # max
    axis1_max = list(matrix.max(axis=0))
    axis2_max = list(matrix.max(axis=1))
    flattened_max = matrix.max()

    # min
    axis1_min = list(matrix.min(axis=0))
    axis2_min = list(matrix.min(axis=1))
    flattened_min = matrix.min()

    # sum
    axis1_sum = list(matrix.sum(axis=0))
    axis2_sum = list(matrix.sum(axis=1))
    flattened_sum = matrix.sum()

    # Instanciar o dicionário solution
    solution = {'mean' : [axis1_mean, axis2_mean, flattened_mean],
                'variance' : [axis1_var, axis2_var, flattened_var],
                'standard deviation' : [axis1_std, axis2_std, flattened_std],
                'max' : [axis1_max, axis2_max, flattened_max],
                'min' : [axis1_min, axis2_min, flattened_min],
                'sum' : [axis1_sum, axis2_sum, flattened_sum]}
    

    return solution