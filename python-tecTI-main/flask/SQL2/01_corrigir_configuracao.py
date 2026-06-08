"""
ATIVIDADE 01 — Configuração Flask + SQLAlchemy

Corrija este arquivo até rodar sem erro:
  python 01_corrigir_configuracao.py

Saída esperada: "Configuração OK! Banco: sqlite:///..."
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# TODO ALUNO: importe SQLAlchemy de flask_sqlalchemy
# from flask_sqlalchemy import ___________


app = Flask(__name__)

pasta = os.path.abspath(os.path.dirname(__file__))

# Configuração correta do banco SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta, "exercicio.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Cria objeto db ligado ao app
db = SQLAlchemy(app)


if __name__ == "__main__":
    # Exibe confirmação de configuração
    print("Configuração OK! Banco:", app.config["SQLALCHEMY_DATABASE_URI"])
    print("Objeto db:", db)