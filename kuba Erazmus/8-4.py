###
# A program that prints your height both in cm and in feet and inches.
#
cm = int(input("Enter your height (in cm): "))
feet = f'{cm//30.48:.0f}'           # <-- The f'{...:.0f}' rounds the number to 0 decimal places
inches = f'{(cm%30.48)/2.54:.0f}'   # <-- The f'{...:.0f}' rounds the number to 0 decimal places

print(f'I am {cm}cm tall, i.e. {feet}ft  and {inches} inches.')