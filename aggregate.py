import sqlite3
import pandas as pd
import time

def generate_report():
    connection = sqlite3.connect('data.db')

    df = pd.read_sql_query('SELECT * FROM MachineData', connection)

    report = df.groupby('MachineID').agg({
        'Temperature': ['min', 'max'],
        'Pressure': ['min', 'max'],
        'Output': ['mean']
    })

    report.columns = ['Min Temperature', 'Max Temperature', 'Min Pressure', 'Max Pressure', 'Mean Output']

    report.to_csv('report.csv', index=False)

    connection.close()

    print("Report saved to report.csv")

while True:
    generate_report()
    time.sleep(86400)  # Generate report every day


