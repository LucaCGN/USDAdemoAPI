# csv_writer.py
# Utility script for writing data to CSV in the ARMS Data API Tester & Explorer application

import csv

def write_to_csv(data, filename):
    """
    Writes the given data to a CSV file with the specified filename.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if isinstance(data, list) and len(data) > 0:
            # Writing headers
            writer.writerow(data[0].keys())
            # Writing data rows
            for row in data:
                writer.writerow(row.values())
        return filename
