# Day 26: 30 Days of python programming

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    techs = ["HTML", "CSS", "Python", "Javascript"]
    return render_template("home.html", techs=techs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        return render_template("post.html")

    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for("result"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
