###
# A program that calculates distance to the horizon from the keyboard
#
import math
h = input ('Enter the height of the observer in meters: ')
h = float(h)
#
#   d = 3.57 * math.sqrt(h) ---> FORMULA
#   d is the distance to horizon in kilometers
# 
d = 3.57 * math.sqrt(h)
print('Your distance from horizon is (in kilometers): ', d)
