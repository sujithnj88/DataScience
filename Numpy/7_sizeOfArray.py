import numpy as np

oneDimArray = np.arange(9)
print(f'oneDimArray.size    :   {oneDimArray.size}')

twoDimArray = oneDimArray.reshape(3, 3)
print(f'twoDimArray.size    :   {twoDimArray.size}')

threeDimArray = np.arange(27).reshape(3, 3, 3)
print(f'threeDimArray.size    :   {threeDimArray.size}')