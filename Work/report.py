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
