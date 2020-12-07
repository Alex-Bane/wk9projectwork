from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    char_class = requests.get("http://service2:5001/char_class")
    race = requests.get("http://service3:5002/race")
    stats = requests.post("http://service4:5003/stats", data=race.text)

    return render_template('index.html', char_class=char_class.text, race=race.text, stats=stats.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
