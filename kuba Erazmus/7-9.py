###
# A program that print the numbers of dice rolled and
# returns True if the number rolled is 1 OR 6
#
import random
dice = random.randint(1,6)                          # <------ Dice max number is 6
special_number = dice == 1 or dice == 6
print(f'Dice rolled: {dice}')
print(f'Special number: {special_number}')