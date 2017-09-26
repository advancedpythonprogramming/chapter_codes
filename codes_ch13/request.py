# request.py

import flask

app = flask.Flask(__name__)


def pow(v1, v2):
    return v1 ** v2


def add(v1, v2):
    return v1 + v2

# Server functions
fun_handle = {'pow': pow, 'add': add}


@app.route('/api/<api_id>')
def api_get(api_id):
    # Request.args contains a dictionary with the
    # arguments that were sent by the client
    args = flask.request.args
    if 'v1' not in args and 'v2' not in args:
        return 'Error: No values were found'
    else:
        # Parse string to integer
        v1 = int(args['v1'])
        v2 = int(args['v2'])

        return '{0}: {1}'.format(api_id, fun_handle[api_id](v1, v2))


if __name__ == '__main__':
    # Start service as port 8080
    app.run(port=8080)
