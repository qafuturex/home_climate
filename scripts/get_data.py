import logging
import time
from typing import Dict

from requests import get
from retry import retry


logger = logging.getLogger(__name__)
HOST = "http://192.168.0.178/json"


@retry((ConnectionError, OSError), delay=30, tries=5, logger=logger)
def get_data() -> Dict:
    logging.info('Read data from weather station')
    try:
        response = get(HOST)
        raw_data = response.json()
    except Exception as error:
        print(error)
        raise

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
