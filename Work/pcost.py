import csv
import sys


# Display total formatted
def display_total(total):
    print(f'Total cost: R{total:.2f}')


# Calculate the total cost of all stocks
def portfolio_cost(csv_file):
    """
    :param csv_file:
    :return: total cost of stocks on provided portfolio
    """
    # Initialise total to R0.0
    total_amount = 0.0
    with open(csv_file) as file:
        rows = csv.reader(file)
        # Discard the titles
        headers = next(rows)
        # Iterate over the stocks and sum all
        try:
            for line in rows:
                shares = int(line[1])
                price = float(line[2])
                total_amount += shares * price
        except ValueError:
            print('Invalid portfolio data structure')
    return total_amount


display_total(portfolio_cost(sys.argv[1]))
