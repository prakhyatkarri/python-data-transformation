import pandas

def read_parquet_data(file_path):
    '''
    This method reads PARQUET content from file at provided file_path and returns the content as Pandas Dataframe
    '''
    try:
        return pandas.read_parquet(file_path, engine='pyarrow')
    except Exception as e:
        print(f'Exception reading file at {file_path}: {e}')
    