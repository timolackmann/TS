from locust import User, task, constant, tag
from pymongo import MongoClient
from time import perf_counter
from datetime import datetime
import greenlet
import random

class Mongo:
    conn = ""

    def __init__(self):
        cs = "mongodb+srv://xxxxx"
        self.conn = MongoClient(cs, connect=False)
        id = ''
    def get_conn(self):
        return self.conn

mongo_client = Mongo()

class Mongouser(User):
    def on_start(self):
        self.id = greenlet.getcurrent().minimal_ident
    @task
    @tag("INSERT")
    def aggregate_test(self):
        with mongo_client.get_conn() as cx:
            db = cx.test

            doc = {
                'id': self.id,
                'reading': 'temperature',
                'measurement': round(random.uniform(-10, 30),4)
            }
            start_time = perf_counter()
            data = db.insert_one(doc)
            duration = perf_counter() - start_time

            if data:
                self.environment.events.request_success.fire(request_type="INSERT", name="Insert test",
                                                             response_time=duration)
            else:
                self.environment.events.request_failure.fire(request_type="INSERT", name="Insert test",
                                                             response_time=duration)
