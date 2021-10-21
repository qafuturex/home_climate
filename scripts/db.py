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


def add_record(temperature,
               humidity,
               pressure,
               altitude):
    logging.info('Put record to database')
    # try:
    cursor.execute(
        f"""
        INSERT INTO climate (`temperature`, `humidity`, `pressure`, `altitude`)
        VALUES ('{temperature}', '{humidity}', '{pressure}', '{altitude}')
        """
    )
    db.commit()


if __name__ == '__main__':
    add_record(temperature=temperature,
               humidity=humidity,
               pressure=pressure,
               altitude=altitude)
