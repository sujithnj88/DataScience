import numpy as np

with open(r"Countries with GDP.txt", "r") as fp:
    fileContent = fp.readlines()
formattedContent = [element.replace("\n", "") for element in fileContent if element != "\n"]

country, GDP = formattedContent[1], formattedContent[-1]

np_country_array = np.array(country.replace("'", "").split(","), dtype='S')
np_GDP_array = np.array(GDP.split(","), dtype='float')

countryWithHighestGDP = np_country_array[np_GDP_array == np.max(np_GDP_array)]
print(f'Country with highest GDP    :   {countryWithHighestGDP[0].decode("ascii")}')

countryWithLowestGDP = np_country_array[np_GDP_array == np.min(np_GDP_array)]
print(f'Country with Lowest GDP    :   {countryWithLowestGDP[0].decode("ascii")}')

for country in np_country_array:
    print(country)

for GDP in np_GDP_array:
    print(GDP)

for data in range(0, len(np_country_array)):
    print(f'Country : {np_country_array[data].decode("ascii")} >> GDP : {np_GDP_array[data]}')

print(f'Highest GDP Value : {np.max(np_GDP_array)}')
print(f'Lowest of GDP Value : {np.min(np_GDP_array)}')
print(f'Mean GDP Value : {np.mean(np_GDP_array)}')
standardisedValue = []
for gdp in np_GDP_array:
    standardisedValue.append((gdp - np.mean(np_GDP_array)) / np.std(np_GDP_array))
print(f'Standardized Value   :   {np.array(standardisedValue)}')
print(f'Sum of GDP Value : {np.sum(np_GDP_array)}')

