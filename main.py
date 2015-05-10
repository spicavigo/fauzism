from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

import logging
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/', methods=['POST', 'GET'])
def hello():
    """Return a friendly HTTP greeting."""
    try:
        logging.warning("Message Received: " + request.form['data'])
    except Exception, e:
        logging.error("Errrrrr!!!")
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
