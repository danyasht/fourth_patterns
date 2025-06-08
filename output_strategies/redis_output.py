from .base import OutputStrategy
import redis
import json

class RedisOutput(OutputStrategy):
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    def write(self, data):
        for row in data:
            key = row.get("Case Number", "unknown")
            value = json.dumps(row, ensure_ascii=False)
            self.client.set(key, value)
        print("[Redis] Data stored in Redis.")
