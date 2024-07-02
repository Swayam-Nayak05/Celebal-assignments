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

