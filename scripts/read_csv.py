import csv

def read_csv_data(file_path):
    '''
    This method reads CSV content from file at provided file_path and returns the content
    '''
    try:
        with open(file_path, 'r') as file:
            content = csv.reader(file, delimiter=",")
            lines=[]

            for row in content:
                lines.append(row)
            
            return lines
    except Exception as e:
        print(f'Exception reading file at {file_path}: {e}')