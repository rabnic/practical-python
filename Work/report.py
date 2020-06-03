import csv


def read_portfolio(portfolio_file):
    """
    :param portfolio_file:
    :return: list of dicts for stock portfolio read from file given
    """
    portfolio_list = []
    with open(portfolio_file) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            dict_holder = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
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

