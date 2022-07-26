import json
import pandas

def read_json_data(file_path):
    '''
    This method reads JSON content from file at provided file_path and returns the content
    '''
    try:
        with open(file_path, 'r') as file:
            content = json.load(file)
            lines = []

            for row in content:
                lines.append(row)
            
            return lines
    except Exception as e:
        print(f'Exception reading file at {file_path}: {e}')
    
