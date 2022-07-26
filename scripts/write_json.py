import json

SAMPLE_JSON_DATA = {
                        'employees' : [
                            {
                                'name' : 'John Doe',
                                'department' : 'Marketing',
                                'place' : 'Remote'
                            },
                            {
                                'name' : 'Jane Doe',
                                'department' : 'Software Engineering',
                                'place' : 'Remote'
                            },
                            {
                                'name' : 'Don Joe',
                                'department' : 'Software Engineering',
                                'place' : 'Office'
                            }
                        ]
                    }

def write_json_data(file_path):
    with open(file_path, 'w') as file:
        json.dump(SAMPLE_JSON_DATA, file)
