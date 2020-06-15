import csv


def parse_csv(filename, select=None):
    """
    Parse a csv file into a list of dict records
    :param filename:
    :return: List of dictionaries
    """
    with open(filename) as file:
        rows = csv.DictReader(file)

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            row = dict(row)
            if select:  # If user wants selected columns
                row = {k: row[k] for k in row.keys() if k in select}
            record = row
            records.append(record)

        return records


print(parse_csv('Data/portfolio.csv', select=['name', 'shares']))
