import numpy as np

firstNumpyArray = np.array([1, 2, 3, 4, 5, 6])
print(firstNumpyArray)

arrayWithZeroes = np.zeros((3, 3))
arrayWithOnes = np.ones((3, 3))
print(f'arrayWithZeroes : {arrayWithZeroes}')
print(f'arrayWithOnes : {arrayWithOnes}')

emptyArray = np.empty((3, 3))
print(f'emptyArray : {emptyArray}')

arrayWithArange = np.arange(15)
print(f'arrayWithArange : {arrayWithArange}')

reshapedArray = arrayWithArange.reshape(3, 5)
print(f'reshapedArray : {reshapedArray}')

lineSpacedArray = np.linspace(1, 5, 10)
print(f'lineSpacedArray : {lineSpacedArray}')
