from pprint import pprint
from random import random
from random import randrange
from random import uniform
from datetime import datetime
from datetime import timedelta
import math


class SampleIOTDevice:

    def __init__(self, sensor_id=1, timestamp=0):
        self.sensor_id = sensor_id
        self.timestamp = timestamp

    def get_temp(self):
        return {
            "metadata": {
                "sensorId": self.sensor_id,
                "type": "temperature"
            },
            # "timestamp": datetime(2021, 7, 22, hour, minute, second, 266943),
            "timestamp": self.timestamp,
            "temp": round(uniform(20, 25), 3)
        }
