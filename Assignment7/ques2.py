import pandas as pd
import os
from sqlalchemy import create_engine

# Set up database connection
db_connection_str = 'postgresql://username:password@localhost/dbname'
db_engine = create_engine(db_connection_str)

# Directory where the files are stored (data lake container)
data_lake_directory = '/path/to/data/lake/container'

# Function to extract date from filename
def extract_date_from_filename(filename):
    date_str = filename.split('_')[-1].split('.')[0]
    date = pd.to_datetime(date_str)
    return date, date_str

# Process CUST_MSTR files
def process_cust_mstr(file_path):
    df = pd.read_csv(file_path)
    date, date_str = extract_date_from_filename(os.path.basename(file_path))
    df['Date'] = date
    df.to_sql('CUST_MSTR', db_engine, if_exists='replace', index=False)

# Process master_child_export files
def process_master_child_export(file_path):
    df = pd.read_csv(file_path)
    date, date_str = extract_date_from_filename(os.path.basename(file_path))
    df['Date'] = date
    df['DateKey'] = date_str
    df.to_sql('master_child', db_engine, if_exists='replace', index=False)

# Process H_ECOM_ORDER files
def process_h_ecom_order(file_path):
    df = pd.read_csv(file_path)
    df.to_sql('H_ECOM_Orders', db_engine, if_exists='replace', index=False)

# Main function to iterate over files and process them
def main():
    for filename in os.listdir(data_lake_directory):
        file_path = os.path.join(data_lake_directory, filename)
        if filename.startswith('CUST_MSTR'):
            process_cust_mstr(file_path)
        elif filename.startswith('master_child_export'):
            process_master_child_export(file_path)
        elif filename.startswith('H_ECOM_ORDER'):
            process_h_ecom_order(file_path)

if __name__ == "__main__":
    main()
