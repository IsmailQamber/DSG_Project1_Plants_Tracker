import csv
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

def plant_care():
    try:
        DF = pd.read_csv('plants.csv')
        for rows in DF.iterrows():
            if rows['record_activity'] == '':
                print(f'plant {rows['plant_name']} needs some care')
    except FileNotFoundError:
        print('There no recorrds for any plant, please enter plants details first')
        return main()