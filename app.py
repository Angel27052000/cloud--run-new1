import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    name=input("Enter your name")
    age=int(input("Enter your age "))
    print("Name",name)
    print("Age")

hello_world()
