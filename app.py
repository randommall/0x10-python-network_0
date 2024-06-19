from flask import (Flask,
                   redirect, request,
                   url_for, jsonify,
                   make_response, abort,
                   Response)
from functools import wraps

app = Flask(__name__)
app.url_map.strict_slashes = False

def allowed_methods(methods=['GET']):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not request.method in methods:
                return abort(405)  # Method Not Allowed
            return function(*args, **kwargs)
        return wrapper
    return decorator


@app.route('/')
def route_0():
    return f'123456789\n', 200


@app.route('/route_1')
def route_1():
    return f'Route 2\n'


@app.route('/route_3', methods=['DELETE'])
def route_3():
    return f"I'm a DELETE request\n"


@app.route('/route_4', methods=['PUT'])
@allowed_methods(['PUT'])
def route_4():
    data = {'mesage': 'Allowed methods'}
    return f'{data}'


@app.route('/route_5')
def route_5():
    if request.headers['X-School-User-Id']:
        return f'Hello School!'
    else:
        return f' "X-School-User-Id" header not included\n'


@app.route('/route_6', methods=['POST'])
def route_6():
    if request.method == 'POST':
        print()
        email = request.form.get('email')
        subject = request.form.get('subject')
        if not email or email != 'test@gmail.com':
            return f'email invalid'
        if not subject or subject != 'I will always be here for PLD':
            return f'subject invalid'
        return f'POST params:\n\temail: {email}\n\tsubject: {subject}\n'


@app.route('/nop')
def nop():
    return f'an error occured!', 404


@app.route('/route_json', methods=['POST'])
def route_json():
    if request.method == 'POST':
        data = request.get_json()
        if type(data) == dict:
            
            return f'Valid JSON\n'
        else:
            return f'Not a valid JSON\n'
    return f'not allowed', 401


@app.route("/catch_me", methods=['PUT'])
def catch_me_1():
    if request.method == 'PUT':
        if request.form.get("user_id") == "98":
            if request.headers.get('Origin') == "School":
                return "You got me!"
            else:
                return "You are not coming from School", 403
        else:
            return "You are not user_id = 98", 401
    else:
        res = Response("No")
        res.headers["Allow"] = "PUT"
        return res
		


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
