import json

from flask import Flask, request

from missile_launcher.missile_launcher import MissileLauncher

app = Flask(__name__)
missile_launcher = MissileLauncher()


@app.route("/fire", methods=['POST'])
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

@app.route("/ping", methods=['GET'])
def ping():
    return "Pong"


def parse_request_data():
    data = json.loads(request.data)
    return data


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
