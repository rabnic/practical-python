# pcost.py
#
# Exercise 1.27

# Initialise total to R0.0
total_amount = 0.0
with open('Data/portfolio.csv', 'rt') as file:
    # Discard the titles
    headers = next(file)
    # Iterate over the stocks and sum all
    for line in file:
        stock_line = line.split(sep=',')
        shares = int(stock_line[1])
        price = float(stock_line[2])
        total_amount += shares * price

print(f'Total cost: R{total_amount:.2f}')
