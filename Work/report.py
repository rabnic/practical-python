import csv


def read_portfolio(portfolio_file):
    """
    :param portfolio_file:
    :return: list of dicts for stock portfolio read from file given
    """
    portfolio_list = []
    with open(portfolio_file) as file:
        rows = csv.reader(file)
        portfolio_headers = next(rows)
        for row in rows:
            record = dict(zip(portfolio_headers, row))
            dict_holder = {"name": record['name'], "shares": int(record['shares']), "price": float(record['price'])}
            portfolio_list.append(dict_holder)
    return portfolio_list


def read_prices(prices_file):
    """

    :param prices_file:
    :return: dict of stock prices where key=stock name and value=price
    """
    with open(prices_file) as file:
        rows = csv.reader(file)
        price_dict = {stock[0]: float(stock[1]) for stock in rows if stock}
    return price_dict


def make_report(portfolio, prices):
    """
    Generate report of stocks profit to current prices
    :param portfolio:
    :param prices:
    :return: list of tuples stock share price from initial purchase
    """
    share_price_list = []
    for stock in portfolio:
        share_price_list.append((stock['name'], stock['shares'], prices[stock['name']],
                                 prices[stock['name']] - stock['price']))
    return share_price_list


portfolio_out = read_portfolio("Data/portfolio.csv")
prices_out = read_prices("Data/prices.csv")

# Display the output in neat aligned tabular form
headers = ("Name", "Shares", "Price", "Change")
line = "-"
print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
print(f"{line*10} {line*10} {line*10} {line*10}")

currency = 'R'

for name, shares, price, change in make_report(portfolio_out, prices_out):
    price = str(round(price, 2))
    print(f"{name:>10s} {shares:>10d} {currency + price:>10s} {change:>10.2f}")
