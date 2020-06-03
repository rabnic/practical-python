import csv


def read_portfolio(portfolio_file):
    """
    :param portfolio_file:
    :return: list of tuples for stock portfolio read from file given
    """
    portfolio_list = []
    with open(portfolio_file) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            portfolio_list.append((row[0], int(row[1]), float(row[2])))
    return portfolio_list
