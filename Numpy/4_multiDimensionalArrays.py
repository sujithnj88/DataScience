import numpy as np

oneDimensionalArray = np.arange(15)
print(f'oneDimensionalArray :   {oneDimensionalArray}')

twoDimensionalArray = oneDimensionalArray.reshape((3, 5))
print(f'twoDimensionalArray :   {twoDimensionalArray}')

threeDimensionalArray = np.arange(27).reshape((3, 3, 3))
print(f'threeDimensionalArray :   {threeDimensionalArray}')
