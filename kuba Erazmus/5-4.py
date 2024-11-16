###
# A program that calculates VAT
#
amount_string = input("Enter the amount: ")
VAT_string = input("Enter VAT (in %): ")
amount = float(amount_string)
VAT = int(VAT_string)
VAT_calc = amount*(VAT/100)
VAT_calc_formatted = f"{VAT_calc:.2f}"
print(f'Amount : {amount_string}')
print(f'VAT {VAT_string}% : {VAT_calc_formatted}')

