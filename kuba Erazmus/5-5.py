###
# A program that calculates and print discounts from input price
#
price_str = input("Enter price: ")
discount_str = input("Enter discount (in %): ")
discount_int = float(discount_str)

price = float(price_str)
price_reduce = (discount_int/100)*price
discounted_price = price - price_reduce

price_reduce_formatted = f"{price_reduce:.2f}"
discounted_price_formatted = f"{discounted_price:.2f}"


print(f'Price with discount: {discounted_price_formatted}')
print(f'Reduction: {price_reduce_formatted}')

