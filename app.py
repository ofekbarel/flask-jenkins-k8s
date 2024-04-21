from flask import Flask, render_template
import os

app = Flask(__name__)



@app.route("/cat")
def hello():
    return render_template('cat.html')


@app.route("/dog")
def hello():
    return render_template('dog.html')


@app.route("/bird")
def hello():
    return render_template('bird.html')


@app.route("/mouse")
def hello():
    return render_template('mouse.html')



@app.route("/")
def hello():
    return "Example app"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)