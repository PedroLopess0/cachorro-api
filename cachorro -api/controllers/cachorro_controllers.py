from models.cachorro_models import Cachorro
from db import db
import json
from flask import make_response, request

def get_cachorros():
    cachorros = Cachorro.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de cachorros.', 
            'dados': [cachorro.json() for cachorro in cachorros]
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
    
def create_cachorro(cachorro_data):
    if not cachorro_data:
        return make_response(json.dumps({'erro': 'JSON ilegítimo ou não enviado'}), 400)

    novo_cachorro = Cachorro(
        nome=cachorro_data.get('nome'),
        raca=cachorro_data.get('raca'),
        idade=cachorro_data.get('idade')
    )
    
    if not novo_cachorro.nome:
        return make_response(json.dumps({'erro': 'O setor "nome" é obrigatório'}), 400)

    db.session.add(novo_cachorro) 
    db.session.commit()
    
    response = make_response(
        json.dumps({
            'cachorro': novo_cachorro.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response