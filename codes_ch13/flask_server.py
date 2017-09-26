# flask_server.py

import flask

app = flask.Flask(__name__)

# Originally, webservers used to have index.html as their main page.
#
# For example, http://mysite.com/index.html.
# By default, when no .html resource is requested
# on the URL root, it is assumed that will return
# the index.html.
#
# Nowadays this structure this folder structure
# is preserved but it is created dynamically catching the
# route and rendering anything we want.


# This route '/' determines the website root.
# Similar to the index.html document.
@app.route('/')
def index():
    return '<h1>Welcome to ur Web Service!</h1>' \
           '<p>HTML content</p>'


# Add a resource section
@app.route('/resources')
def resources_get():
    return "<h1>Resources index</h1>"


# Resource section with arguments
@app.route('/resources/<resource_id>')
def resource_id_get(resource_id):
    return '<p>Looking for resource with id: {}</p>'.format(resource_id)


if __name__ == '__main__':
    # Start service as port 8080
    app.run(port=8080)
