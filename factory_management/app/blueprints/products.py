from flask import Blueprint, request, jsonify
from app.models import Product
from app.decorations import role_required
from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
@role_required('admin')  # Only admin can add products
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201
