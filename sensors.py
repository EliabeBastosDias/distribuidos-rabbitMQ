import random
from kafka import KafkaProducer
import json
import time

class Sensor:
    def __init__(self, sensor_type, sensor_id):
        self.sensor_type = sensor_type
        self.sensor_id = sensor_id

    def read_data(self):
        raise NotImplementedError("Subclasses must implement read_data")


class TemperatureSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__('temperature', sensor_id)

    def read_data(self):
        return {'temperature': round(random.uniform(20, 30), 2)}


class SmokeSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__('smoke', sensor_id)

    def read_data(self):
        return {'smoke_level': round(random.uniform(0, 1), 2)}


class LightSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__('light', sensor_id)

    def read_data(self):
        return {'light_level': round(random.uniform(0, 1000), 2)}


class PresenceSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__('presence', sensor_id)

    def read_data(self):
        return {'presence': random.choice([True, False])}
