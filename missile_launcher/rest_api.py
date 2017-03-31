import json

from flask import Flask, request, Response
from flask_autodoc.autodoc import Autodoc
from pathlib import Path

from missile_launcher.missile_launcher import MissileLauncher

app = Flask(__name__)
auto = Autodoc(app)
missile_launcher = MissileLauncher()


@app.route("/fire", methods=['POST'])
@auto.doc()
def fire():
    data = parse_request_data()
    number_of_shots = data.get('number_of_shots', 1)
    if isinstance(number_of_shots, int):
        missile_launcher.fire(number_of_shots)
    else:
        return "Incorrect argument"

    return "Shooting"

@app.route("/up", methods=['POST'])
def up():
    data = parse_request_data()
    milliseconds = data.get('milliseconds', None)
    if isinstance(milliseconds, int):
        missile_launcher.up(milliseconds)
    else:
        return "Incorrect argument"

    return "Turning up"


@app.route("/down", methods=['POST'])
def down():
    data = parse_request_data()
    milliseconds = data.get('milliseconds', None)
    if isinstance(milliseconds, int):
        missile_launcher.down(milliseconds)
    else:
        return "Incorrect argument"

    return "Turning down"


@app.route("/left", methods=['POST'])
def left():
    data = parse_request_data()
    milliseconds = data.get('milliseconds', None)
    if isinstance(milliseconds, int):
        missile_launcher.left(milliseconds)
    else:
        return "Incorrect argument"

    return "Turning left"


@app.route("/right", methods=['POST'])
def right():
    data = parse_request_data()
    milliseconds = data.get('milliseconds', None)
    if isinstance(milliseconds, int):
        missile_launcher.right(milliseconds)
    else:
        return "Incorrect argument"

    return "Turning right"


@app.route("/reset", methods=['POST'])
def reset():
    missile_launcher.reset()

    return "Resetting"


@app.route("/execute", methods=['POST'])
def execute():
    data = parse_request_data()
    action = data.get('action', "")
    argument = data.get('argument', None)
    if action:
        missile_launcher.execute(action, argument)

    return "Turning right"

@app.route("/developers", methods=['POST', 'PUT'])
def add_developers():
    data = request.data.decode()
    jsonpath = Path("/root/developers.json")
    with jsonpath.open("w") as fo:
         fo.write(data)
    return add_content_type_header(data)

@app.route("/developers", methods=['GET'])
def get_developers():
    jsonpath = Path("/root/developers.json")
    with jsonpath.open() as fo:
        content = fo.read()
        content = add_content_type_header(content)
    return content

@app.route("/ping", methods=['GET'])
def ping():
    return "Pong"


@app.route('/doc', methods=['GET'])
def documentation():
    return auto.html()


def parse_request_data():
    data = json.loads(request.data.decode())
    return data

def add_content_type_header(content):
    return Response(content, mimetype='application/json')

def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
