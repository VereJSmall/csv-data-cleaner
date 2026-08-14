import csv

with open("data/messy_data.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        print(row[0])
