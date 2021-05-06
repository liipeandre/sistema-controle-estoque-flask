from flask import Flask

app = Flask(__name__)

# Configurações de Módulos
import config

# Views
import views.usuario
import views.produto

if __name__ == '__main__':
    app.run()
