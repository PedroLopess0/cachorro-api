from db import db

class Cachorro(db.Model):
    __tablename__ = 'cachorros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    raca = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'raca': self.raca,
            'idade': self.idade
        }