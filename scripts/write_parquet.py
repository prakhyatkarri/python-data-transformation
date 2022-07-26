import pyarrow as pa
import pyarrow.parquet as pq
import pandas

SAMPLE_DATA = ["10","20","30","40","50","60","70"]

def write_parquet_data(file_path):
    df = pandas.DataFrame(SAMPLE_DATA, columns=['Numbers'])
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)