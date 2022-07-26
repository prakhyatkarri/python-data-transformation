from write_json import write_json_data
from write_csv import write_csv_data
from write_yaml import write_yaml_data
from write_parquet import write_parquet_data
from write_avro import write_avro_data

write_json_data('output/json_output.json')
write_csv_data('output/csv_output.csv')
write_yaml_data('output/yaml_output.yaml')
write_parquet_data('output/parquet_output.parquet')   
write_avro_data('output/avro_output.avro')