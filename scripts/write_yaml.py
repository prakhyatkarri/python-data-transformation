import yaml

SAMPLE_DATA = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

def write_yaml_data(file_path):
    with open(file_path, 'w') as file:
        yaml.dump(SAMPLE_DATA, file)