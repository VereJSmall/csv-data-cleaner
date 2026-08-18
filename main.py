import csv

try:
    with open("data/messy_data.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        with open("output/cleaned_data.csv", "w", newline="") as output_file:
            writer = csv.writer(output_file)

            writer.writerow(["Name", "Email", "State"])

            seen = set()

            records_read = 0
            records_written = 0
            duplicates_removed = 0

            for row in reader:
                records_read += 1
                name = row[0].title()
                email = row[1].lower()
                state = row[2].upper()
                customer = (name,
                            email,
                            state,
                            )

                if customer not in seen:
                    seen.add(customer)
                    writer.writerow([name, email, state])
                    records_written += 1
                else:
                    duplicates_removed += 1

    print(
        f"CSV Data Cleaner Complete!\n"
        f"Records Read: {records_read}\n"
        f"Records Written: {records_written}\n"
        f"Duplicates removed: {duplicates_removed}")

except FileNotFoundError:
    print(
        "Error: Could not find 'data/messy_data.csv'.\n"
        "Please make sure the file exists and try again."
    )
