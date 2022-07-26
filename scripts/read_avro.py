from avro.io import DatumReader
from avro.datafile import DataFileReader

def read_avro_data(file_path):
    '''
    This method reads AVRO content from file at provided file_path and returns the content
    '''
    try:
        with open(file_path, 'rb') as file:
            content = DataFileReader(file, DatumReader())
            lines = []

            for row in content:
                lines.append(row)
            
            return lines
    except Exception as e:
        print(f'Exception reading file at {file_path}: {e}')
    