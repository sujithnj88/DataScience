"""
Shape Manipulation are as follows :
    a) Flatten
    b) Reshape
    c) Resize
    d) Split
    e) Stack
"""
import numpy as np

arrayToPerformManipulation = np.arange(27).reshape((3, 3, 3))
print(f'arrayToPerformManipulation : {arrayToPerformManipulation}')

# Flatten the array - Converts multi dimensional array to 1-D array
flattenedArray = np.ravel(arrayToPerformManipulation)
print(f'flattenedArray : {flattenedArray}')

# Reshape an array
reshapedArrayFirstThreeRowNineColumn = flattenedArray.reshape((3, 9))
print(f'reshapedArrayFirstThreeRowNineColumn : {reshapedArrayFirstThreeRowNineColumn}')

# hsplit an array
hSplitArray = np.hsplit(flattenedArray.reshape(3, 9), 3)
print(f'hSplitArray : {hSplitArray}')

# hstack an array
hStackArray = np.hstack(flattenedArray.reshape(3, 9))
print(f'hStackArray : {hStackArray}')

# vsplit an array
vSplitArray = np.vsplit(flattenedArray.reshape(3, 9), 3)
print(f'vSplitArray : {vSplitArray}')

# vstack an array
vStackArray = np.vstack(flattenedArray.reshape(3, 9))
print(f'vStackArray : {vStackArray}')
