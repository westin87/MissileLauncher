from flask import Flask

from missile_launcher.missile_launcher import MissileLauncher

app = Flask(__name__)

@app.route("/fire", methods=['POST'])
def fire():
    missile_launcher = MissileLauncher()
    missile_launcher.fire()

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()