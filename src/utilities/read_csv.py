import csv


def get_csv_data(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
