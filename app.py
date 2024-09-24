from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from db import db  # Importar a instância do banco de dados
from models import Doacao, Voluntario  # Importar os novos modelos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
app.config['SECRET_KEY'] = '231605'
db.init_app(app)  # Inicializar o banco de dados

# Página inicial (exibe as doações e voluntários)
@app.route('/')
def index():
    doacoes = Doacao.query.all()
    voluntarios = Voluntario.query.all()
    return render_template('index.html', doacoes=doacoes, voluntarios=voluntarios)

# Adicionar uma nova doação
@app.route('/adicionar_doacao', methods=['GET', 'POST'])
def adicionar_doacao():
    if request.method == 'POST':
        # Capturando dados do formulário
        nome_doador = request.form['nome_doador']
        quantidade = request.form['quantidade']
        descricao = request.form['descricao']
        data = request.form['data']

        nova_doacao = Doacao(nome_doador=nome_doador, quantidade=quantidade,
                              descricao=descricao, data=data)

        try:
            db.session.add(nova_doacao)
            db.session.commit()
            flash('Doação adicionada com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao adicionar doação: {e}', 'danger')
    
    return render_template('adicionar_doacao.html')

# Adicionar um novo voluntário
@app.route('/adicionar_voluntario', methods=['GET', 'POST'])
def adicionar_voluntario():
    if request.method == 'POST':
        # Capturando dados do formulário
        nome = request.form['nome']
        contato = request.form['contato']
        disponibilidade = request.form['disponibilidade']

        novo_voluntario = Voluntario(nome=nome, contato=contato,
                                      disponibilidade=disponibilidade)

        try:
            db.session.add(novo_voluntario)
            db.session.commit()
            flash('Voluntário adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao adicionar voluntário: {e}', 'danger')
    
    return render_template('adicionar_voluntario.html')

if __name__ == '__main__':
    app.run(debug=True)
