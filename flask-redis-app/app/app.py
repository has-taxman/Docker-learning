from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

# Initialize the visit count key in Redis if it doesn't exist
# if not redis_client.exists('visit_count'):
#    redis_client.set('visit_count', 0)

@app.route('/')
def hello():
    return "Welcome to the Flask Redis App!"

@app.route('/count')
def increment_count():
    # Increment the visit count in Redis
    visit_count = redis_client.incr('visit_count')
    return f"This page has been visited {visit_count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)