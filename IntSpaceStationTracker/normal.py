import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def responses():
    response = requests.get(url="https://api.github.com/")
    track = response.json()
    temp = track["current_user_url"]
    print(temp)
    return f"<h1>Data<p> {temp} </p>"


if __name__ == "__main__":
    app.run(debug=True)
