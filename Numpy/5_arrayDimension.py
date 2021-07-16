import numpy as np

# Dimension of an array is also known as the rank

oneDimArray = np.arange(9)
print(f'oneDimArray.ndim    :   {oneDimArray.ndim}')

twoDimArray = oneDimArray.reshape(3, 3)
print(f'twoDimArray.ndim    :   {twoDimArray.ndim}')

threeDimArray = np.arange(27).reshape(3, 3, 3)
print(f'threeDimArray.ndim    :   {threeDimArray.ndim}')