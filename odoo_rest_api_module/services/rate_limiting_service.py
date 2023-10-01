```python
import redis
from redis.exceptions import ConnectionError

class RateLimitingService:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def increment_counter(self, key):
        try:
            self.redis.incr(key)
        except ConnectionError:
            print("Redis server is not running")

    def get_counter(self, key):
        try:
            return self.redis.get(key)
        except ConnectionError:
            print("Redis server is not running")
            return None

    def set_expiration(self, key, time):
        try:
            self.redis.expire(key, time)
        except ConnectionError:
            print("Redis server is not running")

    def check_rate_limit(self, key, limit):
        counter = self.get_counter(key)
        if counter is not None and int(counter) > limit:
            return False
        return True
```