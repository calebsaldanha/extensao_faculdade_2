from app import app, db
from models import Doacao, Voluntario  # Certifique-se de que está importando todos os modelos que deseja criar

# Crie o contexto da aplicação
with app.app_context():
    db.create_all()  # Cria todas as tabelas definidas nos modelos
    print("Banco de dados criado com sucesso!")
