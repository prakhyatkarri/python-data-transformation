import yaml

def read_yaml_data(file_path):
    '''
    This method reads YAML content from file at provided file_path and returns the content
    '''
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f'Exception reading file at {file_path}: {e}')