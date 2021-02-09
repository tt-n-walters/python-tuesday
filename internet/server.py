# REPL
#   read
#   evaluate
#   print
#   loop

import flask

app = flask.Flask(__name__)


@app.route("/messages")
def request_for_messages():
    response_text = "Server under development. Go away."
    return response_text


app.run(debug=True)
