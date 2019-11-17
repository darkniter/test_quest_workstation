import flask
from flask import render_template, request, jsonify
from random import randint as random
from flask_cors import cross_origin

def init_app():
    app = flask.Flask(__name__)
    return app

app = init_app()

@app.route('/',methods=['GET', 'POST'])
@cross_origin()
def info():
    name_list = ['Великий писатель','Неповторимый философ','Всем известный','Значимой фигурой был',]
    info_list = [ 'И. С. Тургенев','Ф. М. Достоевский',' Л. Н. Толстой','А. П. Чехов']
    
    code_bay = random(0,100000)
    
    data_dict = {
        'name': name_list[random(0,3)],
        'info': info_list[random(0,3)],
        }
    return jsonify({'response':code_bay,'data':data_dict})