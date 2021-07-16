import numpy as np

marksOfTwoStudentsForTwoTests = [[55, 46, 78, 89], [96, 53, 65, 86]]
print(f'marksOfTwoStudentsForTwoTests   :   {marksOfTwoStudentsForTwoTests}')

"""
Currently Student is on X-Axis and Test is on Y-Axis. Which has to be flipped to uniformly display the content
Test information should be on X-Axis and student marks should be seen in reference to Y-Axis
"""
transposeWithFlippedAxis = np.transpose(marksOfTwoStudentsForTwoTests)
print(f'transposeWithFlippedAxis   :   {transposeWithFlippedAxis}')

"""
Inverse : Inverse can be applied to only square matrices (2x2, 3x3, 4x4 ....)
"""
squareMatrixToFindInverse = np.array([[4, 5], [8, 9]])
print(f'squareMatrixToFindInverse   :   {squareMatrixToFindInverse}')
inverseMatrixValue = np.linalg.inv(squareMatrixToFindInverse)
print(f'inverseMatrixValue   :   {inverseMatrixValue}')

"""
Trace : Used to find sum of diagonal elements
"""
arrayToFindSumOfDiagonalElements = np.arange(36).reshape(6, 6)
print(f'arrayToFindSumOfDiagonalElements   :   {arrayToFindSumOfDiagonalElements}')
SumOfDiagonalElementsOfArray = np.trace(arrayToFindSumOfDiagonalElements)
print(f'SumOfDiagonalElementsOfArray   :   {SumOfDiagonalElementsOfArray}')
