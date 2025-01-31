import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_file='finance_data.csv'
    COLUMNS=['date','amount','category','description']

    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df=pd.DataFrame(columns=csv.COLUMNS)
            df.to_csv(cls.CSV_file, index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            'date':date,
            'amount':amount,
            'category':category,
            'description':description
        }
        with open(cls.CSV_file,'a',newline='') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('entry added successfully')

CSV.initialize_csv()
CSV.add_entry('31-01-2025',2500.50,'Income','Salary')