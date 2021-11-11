from flask import Flask, request
from os import getenv

app = Flask("my_app_name")
dbname=getenv('filename_db_cars')


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    my_score = 1
    #result=1/0

    if request.method=='GET':
        my_file = open('cars.txt', 'r')
        return str(my_file.readlines())
    elif request.method=='POST':
        my_file = open('cars.txt', 'w')
        my_file.write(str(request.data))
        my_file.close()
        return 'saved new car'
    else :
        return "<h1>" + str(my_score) + "</h1>"

@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)