"""
Broadcasting is used to carry out arithmetic operations between arrays of different shapes.
In this methos, numpy automatically broadcasts the samaller array over the larger array
"""

import numpy as np

largerArray = np.arange(2)
ElementToMultiply = 0.5

print(largerArray * ElementToMultiply)

"""
ElementToMultiply is broadcasted to each element of the largerArray to perform multiplication operation
Process Follows : 
    a) largerArray[0] * ElementToMultiply
    b) largerArray[1] * ElementToMultiply
    c) largerArray[2] * ElementToMultiply
    
When Numpy operates on two arrays, it compares their shapes element wise. It finds the shape compatible only if
    a) Their dimensions are the same
    b) One of the arrays have a dimension of 1
"""

