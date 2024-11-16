###
# A program that acts like a speed camera
#
speed_input = int(input("Enter vehicle speed (in kph): "))
speed_check = 40 <= speed_input <= 140
print(f'Speed is valid: {speed_check}')