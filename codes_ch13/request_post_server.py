# request_post_server.py

import flask
import json

app = flask.Flask(__name__)


# This time only POST methods
@app.route('/upload', methods=['POST'])
def api_post():
    req = flask.request
    if req.headers['Content-Type'] == 'application/json':
        with open('post.txt', 'w') as fid:
            json.dump(req.json, fid)

        # Send echo to the client
        return "Echo: {}".format(json.dumps(req.json))


if __name__ == '__main__':
    # Start service as port 8080
    app.run(port=8080)
