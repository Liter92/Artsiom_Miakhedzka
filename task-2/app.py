from flask import Flask
import redis
app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
@app.route('/count', methods=['GET'])
def counter():
    inputs = redis_client.incr('inputs')
    return f'Количество обращений: {inputs}\n', 200
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)