import numpy as np
from numpy import pi

testArrayWithFirstTenNumbers = np.arange(11)
print(f'testArrayWithFirstTenNumbers    :   {testArrayWithFirstTenNumbers}')

############################### Universal Functions (ufunc) ###############################
squareRootOfEachNumbers = np.sqrt(testArrayWithFirstTenNumbers)
print(f'squareRootOfEachNumbers    :   {squareRootOfEachNumbers}')

cosValueOfNumbers = np.cos(testArrayWithFirstTenNumbers)
print(f'cosValueOfNumbers    :   {cosValueOfNumbers}')
sinValueOfNumbers = np.sin(testArrayWithFirstTenNumbers)
print(f'sinValueOfNumbers    :   {sinValueOfNumbers}')
tanValueOfNumbers = np.tan(testArrayWithFirstTenNumbers)
print(f'tanValueOfNumbers    :   {tanValueOfNumbers}')

valueOfSinPiByTwo = np.sin(pi / 2)
print(f'valueOfSinPiByTwo    :   {valueOfSinPiByTwo}')

linSpacedArray = np.linspace(1, 20, 50)
flooredArray = np.floor(linSpacedArray)
print(f'flooredArray    :   {flooredArray}')

exponentialArray = np.exp([0, 1, 5])
print(f'exponentialArray    :   {exponentialArray}')
###########################################################################################