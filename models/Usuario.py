from app import app
from database import database


class Usuario(database.Model):

    __tablename__ = 'usuarios'

    idusuario = database.Column(
        database.Integer,
        primary_key=True
    )

    usuario = database.Column(
        database.String(45),
        unique=True,
        nullable=False
    )

    senha = database.Column(
        database.String(255),
        nullable=False
    )

    def validate(self):
        # TODO: Implementar validações de campos
        pass

    def login(self, request):
        return self.query.filter_by(usuario=request.form['usuario']).first()