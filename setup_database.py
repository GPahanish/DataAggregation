import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS MachineData')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS MachineData(
                    MachineID INTEGER,
                    Timestamp TEXT,
                    Temperature REAL,
                    Pressure REAL,
                    Output INTEGER
                )
                ''')

mock_data = [
    (1, '2021-01-01 00:00:00', 100.0, 1000.0, 1),
    (2, '2021-01-01 00:00:01', 100.1, 1000.1, 2),
    (3, '2021-01-01 00:00:02', 100.2, 1000.2, 3),
    (4, '2021-01-01 00:00:03', 100.3, 1000.3, 4),
    (5, '2021-01-01 00:00:04', 100.4, 1000.4, 5),
]

cursor.executemany('''
                     INSERT INTO MachineData(MachineID, Timestamp, Temperature, Pressure, Output)
                     VALUES (?, ?, ?, ?, ?)
                 ''', mock_data)

connection.commit()

print('Data inserted successfully')

connection.close()
