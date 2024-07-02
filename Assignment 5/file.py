# 1)
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import pymysql
def export_data(connection_string, sql_query, csv_path, parquet_path, avro_path):

    df = pd.read_sql(sql_query, connection_string)

    df.to_csv(csv_path, index=False)
    print(f"CSV file saved to: {csv_path}")

    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_path)
    print(f"Parquet file saved to: {parquet_path}")

    schema = {
        "type": "record",
        "name": "myrecord",
        "fields": [{"name": col, "type": str(df[col].dtype)} for col in df.columns]
    }

    with open(avro_path, "wb") as f:
        fastavro.writer(f, schema, records=df.to_records(index=False))
    print(f"Avro file saved to: {avro_path}")


    print(f"Error occurred:")

connection_string = pymysql.connect(db='mydb', user='root', passwd='Swayam@9876', host='127.0.0.1', port=3306)
sql_query = "SELECT * from students"
csv_path = "data.csv"
parquet_path = "data.parquet"
avro_path = "data.avro"

export_data(connection_string, sql_query, csv_path, parquet_path, avro_path)


# 2)
import pandas as pd
from sqlalchemy import create_engine

def copy_selective_data(source_engine_string, target_engine_string, tables_to_copy, columns_to_copy):
  
  source_engine = create_engine(source_engine_string)
  target_engine = create_engine(target_engine_string)

  for customers_1, selected_columns in columns_to_copy.items():
    if not pd.read_sql(f"SHOW TABLES LIKE '{customers_1}'", source_engine).empty:
      print(f"Copying table {customers_1}...")

      sql_query = f"SELECT {', '.join(selected_columns)} FROM {customers_1}"

      try:
        df = pd.read_sql(sql_query, source_engine)
      except Exception as e:
        print(f"Error reading table {customers_1}: {e}")
        continue 
      if not pd.read_sql(f"SHOW TABLES LIKE '{customers_1}'", target_engine).empty:
        print(f"Table {customers_1} already exists in target database. Skipping...")
        continue  

      df.to_sql(students, target_engine, if_exists='replace', index=False)
      print(f"Data copied to table {students} in target database.")
    else:
      print(f"Table {students} not found in source database. Skipping...")


source_engine_string = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Swayam@9876", 
        db='mydb', 
        ) 
      
cur = source_engine_string.cursor()
target_engine_string = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Swayam@9876", 
        db='mydb', 
        ) 
      
ur = target_engine_string.cursor()


tables_to_copy = ["customers_1", "students"]
columns_to_copy = {
  "customers_1": ["acc_no", "name", "acc_type"],
  "students": ["id", "name", "age"]
}

copy_selective_data(source_engine_string, target_engine_string, tables_to_copy, columns_to_copy)
