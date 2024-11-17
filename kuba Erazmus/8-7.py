###
# A program that reads an integer and prints binary and hexadecymal number
#
number = int(input('Enter number: '))
binary = bin(number)
hexa = hex(number)
print(f'Binary number: {binary}')
print(f'Hexadecimal number: {hexa}')