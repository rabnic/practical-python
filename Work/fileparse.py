import csv


def parse_csv(filename):
    """
    Parse a csv file into a list of dict records
    :param filename:
    :return: List of dictionaries
    """
    with open(filename) as file:
        rows = csv.reader(file)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

        return records
