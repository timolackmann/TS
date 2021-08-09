import time
import insert_ts
from datetime import datetime
from datetime import timedelta
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def insert_Data(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)
        insert_ts.insert_data(start_date, end_date, timedelta(seconds=1))
