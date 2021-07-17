import numpy as np

olympicCountryArray = np.array(["Great Britain", "China", "Russia", "United States", "Korea", "Japan", "Germany"])
goldMedalReceivedPerCountry = np.array([29, 38, 24, 46, 13, 7, 11])
silverMedalReceivedPerCountry = np.array([17, 28, 25, 28, 8, 14, 11])
bronzeMedalReceivedPerCountry = np.array([19, 22, 32, 29, 7, 17, 14])

print(f'Country with Maximum Gold Medals is : '
      f'{olympicCountryArray[goldMedalReceivedPerCountry == np.max(goldMedalReceivedPerCountry)]}')
print(f'Countries won more than 20 Golds : {olympicCountryArray[goldMedalReceivedPerCountry > 20]}')
print(f'Countries Medal Tally is as follows : ')
for country in range(0, len(olympicCountryArray)):
    print(f'Country : {olympicCountryArray[country]} >> Gold : {goldMedalReceivedPerCountry[country]} >> '
          f'Silver : {silverMedalReceivedPerCountry[country]} >> Bronze : {bronzeMedalReceivedPerCountry[country]}')
for country in range(0, len(olympicCountryArray)):
    print(f'{olympicCountryArray[country]} holds {goldMedalReceivedPerCountry[country]} Gold medals')
for country in range(0, len(olympicCountryArray)):
    print(f'{olympicCountryArray[country]} has won a total of '
          f'{goldMedalReceivedPerCountry[country] + silverMedalReceivedPerCountry[country] + bronzeMedalReceivedPerCountry[country]} medals')
