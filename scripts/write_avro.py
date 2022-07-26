import json
import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

SCHEMA = {  "type": "record",
            "name": "Employee",
            "fields": [
                {"name": "first_name",       "type": "string"},
                {"name": "last_name",       "type": "string"}
             ]
        }

SAMPLE_DATA = { "first_name": "John", "last_name": "Doe" }


def write_avro_data(file_path):
    with open(file_path, 'wb') as file:
        schema = avro.schema.parse(json.dumps(SCHEMA))
        writer = DataFileWriter(file, DatumWriter(), schema)
        writer.append(SAMPLE_DATA)
        writer.close()