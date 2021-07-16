import numpy as np

oneDimArray = np.arange(9)
print(f'oneDimArray.dtype    :   {oneDimArray.dtype}')

#################################################################################################
# Data types declaration during array creation
floatArray = np.arange(9, dtype='float')
print(f'floatArray.dtype    :   {floatArray.dtype}')
complexArray = np.arange(9, dtype='complex')
print(f'complexArray.dtype    :   {complexArray.dtype}')
stringArray = np.array(["I", "AM", "SUJITH", "N", "JANARDANAN"], dtype='S')
print(f'stringArray.dtype    :   {stringArray.dtype}')
#################################################################################################

twoDimArray = oneDimArray.reshape(3, 3)
print(f'twoDimArray.dtype    :   {twoDimArray.dtype}')

threeDimArray = np.arange(27).reshape(3, 3, 3)
print(f'threeDimArray.dtype    :   {threeDimArray.dtype}')