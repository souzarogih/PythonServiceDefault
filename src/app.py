import logging as log
from config.env_config import env
from flask_restful import Api
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env.get("DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    return '<h1>Service Default UP</h1>'


if __name__ == '__main__':
    # from sql_alchemy import banco
    # banco.init_app(app)
    log.info("Aplicação executada!!!")
    # app.run(debug=True,  port=os.getenv("APP_PORT")) # usar para rodar via terminal
    # app.run(host="0.0.0.0", debug=True, port=8080)
    app.run(debug=True)