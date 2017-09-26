# request_response_server.py

import flask
import json


def get_id():
    pid = 0
    while True:
        yield pid
        pid += 1

pid = get_id()


class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.id = next(pid)


app = flask.Flask(__name__)


# Response to GET method at /api route
@app.route('/api', methods=['GET'])
def api_echo():
    person = Person('Jason Kruger', '20.000.000-0')
    return flask.Response(json.dumps(person.__dict__), status=200)


if __name__ == '__main__':
    # Start service as port 8080
    app.run(port=8080)
