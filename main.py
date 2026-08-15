import csv

with open("data/messy_data.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    with open("output/cleaned_data.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Name", "Email", "State"])

        for row in reader:
            name = row[0].title()
            email = row[1].lower()
            state = row[2].upper()

            writer.writerow([name, email, state])
