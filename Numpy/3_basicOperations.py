import numpy as np

#######################################################################################################################
# Arithmetic Operation
cyclistOneTravelDistance = range(10, 50, 10)
cyclistTwoTravelDistance = range(0, 20, 5)
timeDriven = [5, 8, 7, 4]

# Addition Operation
totalDistanceArray = np.array(cyclistOneTravelDistance) + np.array(cyclistTwoTravelDistance)
print(f'totalDistanceArray  :   {totalDistanceArray}')

differenceDistanceTravelled = np.array(cyclistOneTravelDistance) - np.array(cyclistTwoTravelDistance)
print(f'differenceDistanceTravelled  :   {differenceDistanceTravelled}')

totalDistanceTravelledForFiveDays = totalDistanceArray * 5
print(f'totalDistanceTravelledForFiveDays  :   {totalDistanceTravelledForFiveDays}')

speedOfCyclists = totalDistanceArray / np.array(timeDriven)
print(f'speedOfCyclists  :   {speedOfCyclists}')

sumOfTotalDistanceArray = sum(totalDistanceArray)
print(f'sumOfTotalDistanceArray  :   {sumOfTotalDistanceArray}')
#######################################################################################################################

#######################################################################################################################
# Logical Operation
dailyPhoneUsageForAWeek = [12, 14, 5, 13, 4, 1, 6]

phoneUsageGreaterThanFourAndLessThanTen = np.logical_and(np.array(dailyPhoneUsageForAWeek) > 4,
                                                         np.array(dailyPhoneUsageForAWeek) < 10)
print(f'phoneUsageGreaterThanFourAndLessThanTen :   {phoneUsageGreaterThanFourAndLessThanTen}')

phoneUsageNotGreaterThanFour = np.logical_not(np.array(dailyPhoneUsageForAWeek) > 4)
print(f'phoneUsageNotGreaterThanFour :   {phoneUsageNotGreaterThanFour}')
#######################################################################################################################

#######################################################################################################################
# Comparison Operator
rohitSharmaLastTenODIScore = [37, 25, 28, 119, 42, 10, 63, 159, 36, 56]
weeklyWorkingHours = [42, 38, 49, 36, 45]

rohitInningsMoreThanFifty = np.array(rohitSharmaLastTenODIScore)[np.array(rohitSharmaLastTenODIScore) > 50]
print(f'rohitInningsMoreThanFifty  :   {rohitInningsMoreThanFifty}')

rohitInningsLessThanFifty = np.array(rohitSharmaLastTenODIScore)[np.array(rohitSharmaLastTenODIScore) < 50]
print(f'rohitInningsLessThanFifty  :   {rohitInningsLessThanFifty}')

rohitInningsNotEqualToFifty = np.array(rohitSharmaLastTenODIScore)[np.array(rohitSharmaLastTenODIScore) != 50]
print(f'rohitInningsNotEqualToFifty  :   {rohitInningsNotEqualToFifty}')
#######################################################################################################################
