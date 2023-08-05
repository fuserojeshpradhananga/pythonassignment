import csv

def filter_adults(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = [row for row in csv_reader if int(row['Age']) >= 18]

    with open(output_file, 'w', newline='') as csv_output:
        fieldnames = ['Name', 'Age']
        csv_writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(rows)

if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "adults.csv"
    filter_adults(input_file, output_file)
