from .base import OutputStrategy
from kafka import KafkaProducer
import json

class KafkaOutput(OutputStrategy):
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = 'crime-data'

    def write(self, data):
        for row in data:
            self.producer.send(self.topic, row)
        self.producer.flush()
        print("[Kafka] Data sent to topic.")
