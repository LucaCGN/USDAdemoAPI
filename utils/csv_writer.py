import csv
import os

def write_to_csv(data, filename):
    """
    Writes the given data to a CSV file with the specified filename.
    Creates necessary directories if they do not exist.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if isinstance(data, list) and len(data) > 0:
            writer.writerow(data[0].keys())  # Writing headers
            for row in data:
                writer.writerow(row.values())
        elif isinstance(data, dict):
            writer.writerow(data.keys())
            writer.writerow(data.values())
        return filename
