from pymongo import MongoClient
from datetime import date, datetime, timedelta
from sample_data import SampleIOTDevice

client = MongoClient(
    'mongodb+srv://xx')
db = client['POVTS']


def insert_data(start_date, end_date, delta=timedelta(seconds=1)):
    current_date = start_date
    data = []
    while current_date < end_date:
        sample_data_object = SampleIOTDevice('1', current_date)
        datapoint = sample_data_object.get_temp()
        data.append(datapoint)
        if len(data) > 4000:
            insert = db['sensorData'].insert_many(data)
            data = []
        # yield current_date
        current_date += delta

    insert = db['sensorData'].insert_many(data)
