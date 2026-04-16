from flask import Blueprint, request
from controllers.cachorro_controllers import get_cachorros, create_cachorro

cachorro_routes = Blueprint('cachorro_routes', __name__)

@cachorro_routes.route('/Cachorro', methods=['GET'])
def cachorros_get():
    return get_cachorros()

@cachorro_routes.route('/Cachorro', methods=['POST'])
def cachorros_post():
    return create_cachorro(request.json)