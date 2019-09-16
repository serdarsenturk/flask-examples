from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/cookie')
def index():
    cookie = request.cookies.get('secret-token')
    if not cookie:
        return "unauthorized", 401
    elif cookie != 'random string':
        return "wrong", 403
    else:
        return "Woohoo"


@app.route('/')
def setNewCookie():
    resp = make_response("new cookie")
    resp.set_cookie('secret-token', 'random string')
    return resp

app.run()