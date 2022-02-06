import logging
import mysql.connector

from get_data import get_data

data = get_data()
temperature = data['temperature']
humidity = data['humidity']
pressure = data['pressure']
altitude = data['altitude']

config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'auth_plugin': 'mysql_native_password',
    'database': 'home_climate'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
climate = cursor.execute("SELECT * FROM climate")
for x in cursor:
    print(x)


def add_record(temp, hum, press, alt):
    logging.info('Put record to database')
    # TODO add retry here too
    cursor.execute(
        f"""
        INSERT INTO climate (`temperature`, `humidity`, `pressure`, `altitude`)
        VALUES ('{temp}', '{hum}', '{press}', '{alt}')
        """
    )
    db.commit()


if __name__ == '__main__':
    add_record(temp=temperature,
               hum=humidity,
               press=pressure,
               alt=altitude)
