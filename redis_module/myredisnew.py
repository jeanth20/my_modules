import redis
import json
import pprint

class MyRedis:
    # Connection Management    
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        self.redis_host = host
        self.redis_port = port
        self.redis_db = db
        self.redis_password = password
        self.conn = redis.Redis(
            host=self.redis_host,
            port=self.redis_port,
            db=self.redis_db,
            password=self.redis_password
        )

    # Basic Operations
    def get(self, key):
        # Retrieve the value associated with a key.
        try:
            return self.conn.get(key)
        except redis.RedisError as e:
            return(f"Error: {e}")
    
    def set(self, key, value):
        # Set the value for a given key.
        try:
            return self.conn.set(key, value)
        except redis.RedisError as e:
            return(f"Error: {e}")
            
    def delete(self, key):
        # Delete a key and its associated value.
        try:
            return self.conn.delete(key)
        except redis.RedisError as e:
            return(f"Error: {e}")
    
    def exists(self, key):
        # Check if a key exists in Redis.
        try:
            return self.conn.exists(key)
        except redis.RedisError as e:
            return(f"Error: {e}")
            
    def get_all_keys(self, pretty_print=False):
        try:
            keys = self.conn.keys('*')
            items = [key.decode() for key in keys]        
            if pretty_print:
                pprint.pprint(items)
            else:
                return items
        except redis.RedisError as e:
            return(f"Error: {e}")

    def get_all_values(self, pretty_print=False):
        try:
            keys = self.conn.keys('*')
            values = []
            for key in keys:
                value = self.conn.get(key)
                values.append(value.decode() if value else None)
            if pretty_print:
                pprint.pprint(values)
            else:
                return values
        except redis.RedisError as e:
            return(f"Error: {e}")
            
    def get_all_items(self, pretty_print=False):
        try:
            keys = self.conn.keys('*')
            items = {}
            for key in keys:
                value = self.conn.get(key)
                items[key.decode()] = value.decode() if value else None

            if pretty_print:
                pprint.pprint(items)
            else:
                return items
        except redis.RedisError as e:
            return(f"Error: {e}")
            
    # Data Structures and Complex Operations
    def string_get(self, key):
        # Retrieve a string value associated with a key.
        try:
            return self.conn.get(key)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def string_set(self, key, value):
        # Set a string value for a given key.
        try:
            return self.conn.set(key, value)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def list_push_left(self, key, *values):
        # Push one or multiple values to the left end of a list.
        try:
            return self.conn.lpush(key, *values)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def list_push_right(self, key, *values):
        # Push one or multiple values to the right end of a list.
        try:
            return self.conn.rpush(key, *values)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def list_get_range(self, key, start=0, end=-1):
        # Get a range of elements from a list.
        try:
            return self.conn.lrange(key, start, end)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def set_add(self, key, *values):
        # Add one or multiple values to a set.
        try:
            return self.conn.sadd(key, *values)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def set_get(self, key):
        # Retrieve all values from a set.
        try:
            return self.conn.smembers(key)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def set_remove(self, key, *values):
        # Remove one or multiple values from a set.
        try:
            return self.conn.srem(key, *values)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def hash_set(self, key, field, value):
        # Set a field-value pair in a hash.
        try:
            return self.conn.hset(key, field, value)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def hash_get(self, key, field):
        # Retrieve the value associated with a field in a hash.
        try:
            return self.conn.hget(key, field)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def hash_get_all(self, key):
        # Retrieve all field-value pairs from a hash.
        try:
            return self.conn.hgetall(key)
        except redis.RedisError as e:
            return(f"Error: {e}")

    def sorted_set_add(self, key, value, score):
        # Add a value with a score to a sorted set.
        try:
            return self.conn.zadd(key, {value: score})
        except redis.RedisError as e:
            return(f"Error: {e}")

    def get_range_sorted_set(self, key, start=0, end=-1):
        # Get a range of elements from a sorted set.
        try:
            return self.conn.zrange(key, start, end)
        except redis.RedisError as e:
            return(f"Error: {e}")
            

# Example usage
redis_instance = MyRedis()

# Get all items and pprint the result
redis_instance.get_all_items(pretty_print=True)

# Get all items and return the result
result = redis_instance.get_all_items()
print(result)

# Other function calls...
