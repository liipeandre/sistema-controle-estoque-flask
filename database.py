from app import app

from flask_sqlalchemy import SQLAlchemy


username = 'root'
password = ''
server = 'localhost'
database_name = 'sistemacontroleestoque'


def get_connection():
    config = "mysql://{username}:{password}@{server}/{database}".format(
        username=username,
        password=password,
        server=server,
        database=database_name
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = config

    return SQLAlchemy(app)


database = get_connection()
