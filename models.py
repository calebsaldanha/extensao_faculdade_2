from db import db

# Tabela de doações
class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_doador = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'Doacao({self.nome_doador}, {self.quantidade})'

# Tabela de voluntários
class Voluntario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100), nullable=False)
    disponibilidade = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Voluntario({self.nome}, {self.contato})'
