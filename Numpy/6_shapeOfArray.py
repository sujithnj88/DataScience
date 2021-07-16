import numpy as np

oneDimArray = np.arange(9)
print(f'oneDimArray.shape    :   {oneDimArray.shape}')

twoDimArray = oneDimArray.reshape(3, 3)
print(f'twoDimArray.shape    :   {twoDimArray.shape}')

threeDimArray = np.arange(27).reshape(3, 3, 3)
print(f'threeDimArray.shape    :   {threeDimArray.shape}')