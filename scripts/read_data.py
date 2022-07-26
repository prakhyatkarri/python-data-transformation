from read_json import read_json_data
from read_csv import read_csv_data
from read_yaml import read_yaml_data
from read_parquet import read_parquet_data
from read_avro import read_avro_data

# File Paths
json_file_path = 'data/population.json'
csv_file_path = 'data/equipment.csv'
yaml_file_path = 'data/invoice.yaml'
parquet_file_path = 'data/yellowtaxi.parquet'
avro_file_path = 'data/train.avro'

# Reading File Content
json_file_content = read_json_data(json_file_path)
print(f'Json File Content: {json_file_content}')

csv_file_content = read_csv_data(csv_file_path)
print(f'CSV File Content: {csv_file_content}')

yaml_file_content = read_yaml_data(yaml_file_path)
print(f'YAML File Content: {yaml_file_content}')

parquet_file_content = read_parquet_data(parquet_file_path)
print(f'Parquet File Content: {parquet_file_content}')

avro_file_content = read_avro_data(avro_file_path)
print(f'Avro File Content: {avro_file_content}')

