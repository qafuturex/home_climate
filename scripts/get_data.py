import logging
from typing import Dict
from requests import get


HOST = "http://192.168.0.178/json"

# TODO: add retry, if request return exception


def get_data() -> Dict:
    logging.info('Read data from weather station')
    raw_data = get(HOST).json()
    temperature = round(float(raw_data['temperature']), 1)
    humidity = round(float(raw_data['humidity']))
    pressure = round(float(raw_data['pressure']))
    altitude = round(float(raw_data['altitude']))
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'altitude': altitude
    }

    return data


if __name__ == '__main__':
    get_data()
