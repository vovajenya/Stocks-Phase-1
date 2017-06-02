import csv

filename = "C:\\Users\\elahav109995\\PycharmProjects\\Phase1_stocks\\companies1.csv"


def get_list():

    symbols = list()
    company_name = list()

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            symbols.append(row[0])
            company_name.append(row[1])



    return symbols, company_name