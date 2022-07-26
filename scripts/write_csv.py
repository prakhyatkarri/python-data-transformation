import csv
HEADER = ['first_name', 'last_name']
SAMPLE_DATA = [['John','Doe'],['Jane','Doe']]

def write_csv_data(file_path):
    with open(file_path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        
        for row in SAMPLE_DATA:
            writer.writerow(row)