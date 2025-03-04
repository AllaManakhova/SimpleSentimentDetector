import csv


def rusentilex_2017_handler():
    rusentilex_2017 = []

    with open(
            "rusentilex-2017.csv", 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            if '' not in row:
                rusentilex_2017.append(row)

    return rusentilex_2017


rusentilex_2017_handler()
