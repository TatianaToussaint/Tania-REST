import csv


def get_rows(csvfile):
    rows = []
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            rows.append(row)
    return rows

#print(get_rows("../get_tests/airports.csv"))