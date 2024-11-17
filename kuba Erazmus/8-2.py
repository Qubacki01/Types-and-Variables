###
# Calculation of circle area and circumference 
#
# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
import math
r = float(input("Enter radius: "))
PI = math.pi
area_calc = PI*r**2
circumference_calc = 2*PI*r
area = f'{area_calc:.2f}'
circumference = f'{circumference_calc:.2f}'
print(f'Circle area is: {area}')
print(f'Circle circumference is: {circumference}')
