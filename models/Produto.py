from app import app
from database import database


class Produto(database.Model):

    __tablename__ = 'produtos'

    idproduto = database.Column(
        database.Integer,
        primary_key=True
    )

    nome = database.Column(
        database.String(45),
        nullable=False
    )


    quantidade = database.Column(
        database.Integer,
        nullable=False
    )


    categoria = database.Column(
        database.String(45),
        nullable=False
    )

    def insert(self, request):
        produto = Produto(
            nome=request.form['nome'],
            quantidade=request.form['quantidade'],
            categoria=request.form['categoria'],
        )

        database.session.add(produto)
        database.session.commit()

    def delete(self, request):
        produto = self.query.get(request.values['idproduto'])
        database.session.delete(produto)
        database.session.commit()

    def list(self, request):
        return self.query.all()

    def view(self, request):
        return self.query.filter_by(idproduto=request.values['idproduto']).first()

    def edit(self, request):
        produto = self.query.get(request.values['idproduto'])

        produto.nome = request.values['nome']
        produto.quantidade = request.values['quantidade']
        produto.categoria = request.values['categoria']

        database.session.commit()