###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
temp_C = float(input("Enter temperature (in Celsius): "))   # <-- User enters value in °C (float)
temp_K = temp_C + 273.15                                    # <-- Calculation to Kelvin
temp_F = temp_C * 1.8 + 32                                  # <-- Calculation to Fahrenheit

print(f'Temperature in Celsius: {temp_C}°C')                #
print(f'Temperature in Kelvin: {temp_K}K')                  # <-- Print calculated values
print(f'Temperature in Fahrenheit: {temp_F}°F')             #

