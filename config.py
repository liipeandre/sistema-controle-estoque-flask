from app import app

# Chave secreta para sessão
app.config['SECRET_KEY'] = 'secret_key'

# Desabilita eventos do SQL Alchemy (não necessário)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False