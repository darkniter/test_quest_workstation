import flask
from flask import render_template, request, jsonify
from random import randint as random

def init_app():
    app = flask.Flask(__name__)
    return app

app = init_app()

@app.route('/',methods=['GET', 'POST'])
def info():
    name_list = ['Великий','Неповторимый','Писатель','Драматург','Значимый',]
    info_list = [ 'И. С. Тургенев','Ф. М. Достоевский',' Л. Н. Толстой','А. П. Чехов']
    
    code_bay = random(0,100000)
    
    data_dict = {
        'name': name_list[random(0,4)],
        'info': info_list[random(0,3)],
        }
    return jsonify({'response':code_bay,'data':data_dict})