from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/char_class', methods=['GET'])
def char_class():
    char_class = ["Fighter", "Rogue", "Wizard", "Ranger", "Cleric"]


    return Response(random.choice(char_class), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
