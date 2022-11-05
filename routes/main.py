from app import app
from flask import render_template

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/route_11')
def route_1():
    return("hello agin")

@app.route("/hello/<string:name>/<string:last_name>")
def hello_user(name, last_name):
    return render_template("index.html", name=name, last_name=last_name)

@app.route("/calc/<int:num_1>/<int:num_2>")
def calc(num_1, num_2):
    sum = (num_1 + num_2)
    return render_template("result.html", sum=sum)




# @app.route("/news/<int:id>")
# def news(id):
#     #news= SELECT * FROM news WHERE id=id
#     return news
