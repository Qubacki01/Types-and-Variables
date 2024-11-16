###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
b_string = input('b=')
c_string = input('c=')
a = int(a_string)
b = int(b_string)
c = int(c_string)
cuboid_volume = a*b*c
cuboid_surface_area = 2*a*b + 2*b*c + 2*a*c
print(f'The volume of a cuboid with side lenghts of: a = {a_string}, b = {b_string} and c = {c_string} is: {cuboid_volume}')
print(f'The surface area of a cuboid with side lenghts of: a = {a_string}, b = {b_string} and c = {c_string} is: {cuboid_surface_area}')