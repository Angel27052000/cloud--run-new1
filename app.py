import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def user_details():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        return render_template("user_details.html", name=name, age=age)
    return render_template("user_details.html")

if __name__ == "__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")

