import csv


def read_portfolio(portfolio_file) -> list:
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


def read_prices(prices_file) -> dict:
    """
    :param prices_file:
    :return: dict of stock prices where key=stock name and value=price
    """
    with open(prices_file) as file:
        rows = csv.reader(file)
        price_dict = {stock[0]: float(stock[1]) for stock in rows if stock}
    return price_dict


def make_report(portfolio, prices) -> list:
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


def display_headers(headers_in):
    """
    Display the headers and line dividers of fixed size
    :param headers_in:
    """
    print('%10s %10s %10s %10s' % headers_in)
    print(('-' * 10 + ' ') * len(headers_in))


def print_report(portfolio):
    """
    Display the full portfolio report in a tabular form
    :param portfolio of stocks
    """
    currency = 'R'
    for name, shares, price, change in portfolio:
        price = str(round(price, 2))
        print(f"{name:>10s} {shares:>10d} {currency + price:>10s} {change:>10.2f}")


portfolio_out = read_portfolio("Data/portfolio.csv")
prices_out = read_prices("Data/prices.csv")
headers = ("Name", "Shares", "Price", "Change")

display_headers(headers)
print_report(make_report(portfolio_out, prices_out))
