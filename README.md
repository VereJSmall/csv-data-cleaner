# CSV Data Cleaner

A Python application that cleans customer CSV files by formatting data, removing duplicate records, and exporting a clean dataset.

## Features

- Reads customer data from a CSV file
- Formats names using title case
- Converts email addresses to lowercase
- Converts state abbreviations to uppercase
- Removes duplicate customer records
- Exports cleaned data to a new CSV file
- Displays processing statistics
- Handles missing input files gracefully

## Technologies Used

- Python 3
- CSV module
- Git
- GitHub

## Project Structure

```text
csv-data-cleaner/
├── data/
│   └── messy_data.csv
├── output/
│   └── cleaned_data.csv
├── main.py
└── README.md
```

## How to Run

```bash
git clone https://github.com/VereJSmall/csv-data-cleaner.git

cd csv-data-cleaner

python3 main.py
```

## Example Output

```text
CSV Data Cleaner Complete!

Records Read: 4
Records Written: 3
Duplicates Removed: 1
```

## Skills Demonstrated

- File handling
- CSV processing
- Data cleaning
- Duplicate detection using sets
- Error handling
- Loops
- Conditional statements
- Tuples
- Git
- GitHub

## Future Improvements

- Support Excel (.xlsx) files
- Allow custom input/output filenames
- Command-line arguments
- Logging
- Graphical user interface (GUI)

## Author

Vere Jaden Small
