from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/before")
def before():
    return render_template("before.html")


@app.route("/after")
def after():
    return render_template("after.html")


if __name__ == "__main__":
    app.run(debug=True)
