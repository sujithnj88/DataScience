import numpy as np

placesToVisitOnWorldTour = np.array(["Paris", "Tahiti", "Berlin", "Rome", "Amsterdam", "Tokyo", "Barcelona",
                                     "Maldives"])
print(f'placesToVisitOnWorldTour :   {placesToVisitOnWorldTour}')

# Deep copy. New copy of array will be generated and any changes made to new array will not affect the original array
# content
copiedArray = placesToVisitOnWorldTour.copy()
print(f'copiedArray :   {copiedArray}')
copiedArray[-1] = "Grand Canyon"
print(f'copiedArray :   {copiedArray}')
print(f'placesToVisitOnWorldTour :   {placesToVisitOnWorldTour}')

# Shallow Copy (View). Any changes done to the view will affect the original array also
arrayView = placesToVisitOnWorldTour.view()
print(f'arrayView :   {arrayView}')
arrayView[-1] = "Grand Canyon"
print(f'arrayView :   {arrayView}')
print(f'placesToVisitOnWorldTour :   {placesToVisitOnWorldTour}')
