import numpy as np

###################################################################################################################
testArray = np.arange(9).reshape(3, 3)
print(f'testArray   :   {testArray}')

firstArrayElement = testArray[0]
print(f'firstArrayElement   :   {firstArrayElement}')
firstElem, secondElem, thirdElem = firstArrayElement[0], firstArrayElement[1], firstArrayElement[2]
print(f'firstElem : {firstElem} >> secondElem : {secondElem} >> thirdElem : {thirdElem} \n')

secondArrayElement = testArray[1]
print(f'secondArrayElement   :   {secondArrayElement}')
firstElem, secondElem, thirdElem = secondArrayElement[0], secondArrayElement[1], secondArrayElement[2]
print(f'firstElem : {firstElem} >> secondElem : {secondElem} >> thirdElem : {thirdElem}\n')

thirdArrayElement = testArray[2]
print(f'thirdArrayElement   :   {thirdArrayElement}')
firstElem, secondElem, thirdElem = thirdArrayElement[0], thirdArrayElement[1], thirdArrayElement[2]
print(f'firstElem : {firstElem} >> secondElem : {secondElem} >> thirdElem : {thirdElem}\n')

allElementsOfSecondDimension = testArray[1, :]
print(f'allElementsOfSecondDimension    :   {allElementsOfSecondDimension}')
allElementsOfFirstAndSecondDimension = testArray[:2, :]
print(f'allElementsOfFirstAndSecondDimension    :   {allElementsOfFirstAndSecondDimension}')
lastTwoElementsOfAllDimensions = testArray[:, 1:]
print(f'lastTwoElementsOfAllDimensions    :   {lastTwoElementsOfAllDimensions}')
###################################################################################################################

###################################################################################################################
# Indexing with Boolean
booleanExpression = testArray > 5
print(f'booleanExpression   :   {booleanExpression}')
booleanIndexedArray = testArray[booleanExpression]
print(f'booleanIndexedArray :   {booleanIndexedArray}')
###################################################################################################################
