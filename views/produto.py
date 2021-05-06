from flask import request, render_template, url_for, redirect, flash
from app import app

from models.Produto import Produto


@app.route('/main/produtos/insert', methods=['GET', 'POST'], endpoint='produto.insert')
def insert():
    if request.method == 'GET':
        return render_template('produtos/insert.html')

    else:
        nome = request.form.get('nome', '')
        quantidade = request.form.get('quantidade', '')
        categoria = request.form.get('categoria', '')

        categorias = ['Informática', 'Telefonia', 'Moda', 'Eletrodomésticos', 'Automotivo', 'Pet Shop']

        if not nome or len(nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not quantidade or not quantidade.isdigit() or int(quantidade) < 0:
            flash("Campo 'quantidade' é obrigatório e deve ser numérico.")

        elif not categoria or categoria not in categorias:
            flash("Campo 'categoria' é obrigatório ou é inválido.")

        else:
            model = Produto()
            model.insert(request)
            flash('Produto inserido com sucesso.')

        return render_template('produtos/insert.html')


@app.route('/main/produtos/delete', methods=['GET'], endpoint='produto.delete')
def delete():
    idproduto = request.values.get('idproduto', '')

    if not idproduto or not idproduto.isdigit() or int(idproduto) <= 0:
        flash("Campo 'idproduto' é obrigatório e deve ser numérico.")

    else:
        model = Produto()
        model.delete(request)
        flash('Produto excluído com sucesso.')

    return redirect(url_for('produto.list'))


@app.route('/main/produtos', methods=['GET'], endpoint='produto.list')
def list():
    model = Produto()
    produtos = model.list(request)
    return render_template('produtos/list.html', produtos=produtos)


@app.route('/main/produtos/edit', methods=['GET', 'POST'], endpoint='produto.edit')
def edit():
    if request.method == 'GET':
        idproduto = request.values.get('idproduto', '')

        if not idproduto or not idproduto.isdigit() or int(idproduto) <= 0:
            flash("Campo 'idproduto' é obrigatório e deve ser numérico.")
            return redirect(url_for('produto.list'))

        else:
            model = Produto()
            produto = model.view(request)
            return render_template('produtos/edit.html', produto=produto)

    else:
        idproduto = request.form.get('idproduto', '')
        nome = request.form.get('nome', '')
        quantidade = request.form.get('quantidade', '')
        categoria = request.form.get('categoria', '')

        categorias = ['Informática', 'Telefonia', 'Moda', 'Eletrodomésticos', 'Automotivo', 'Pet Shop',]

        if not idproduto or not idproduto.isdigit() or int(idproduto) <= 0:
            flash("Campo 'idproduto' é obrigatório e deve ser numérico.")

        if not nome or len(nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not quantidade or not quantidade.isdigit() or int(quantidade) < 0:
            flash("Campo 'quantidade' é obrigatório e deve ser numérico.")

        elif not categoria or categoria not in categorias:
            flash("Campo 'categoria' é obrigatório ou é inválido.")

        else:
            model = Produto()
            model.edit(request)
            flash('Produto alterado com sucesso.')

        return render_template('produtos/edit.html', produto=request.form)