from flask import Blueprint, request
from models.products import Products, ProductsSchema
from utils.config import db

productsRoutes = Blueprint('products', __name__)

productSchema = ProductsSchema()
productsSchema = ProductsSchema(many = True)

@productsRoutes.route('/products', methods = ['POST'])
def setProduct():
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    
    newProduct = Products(name, price, description)

    db.session.add(newProduct)
    db.session.commit()
    
    return productSchema.jsonify(newProduct)

@productsRoutes.route('/products')
def getProducts():

    allProducts = Products.query.all()
    result = productsSchema.dump(allProducts)

    return productsSchema.jsonify(result)

@productsRoutes.route('/products/<id>')
def getProduct(id):
    product = Products.query.get(id)
    return productSchema.jsonify(product)     


@productsRoutes.route('/products/<id>', methods=['PUT'])
def updateProduct(id):
    product = Products.query.get(id)

    name = request.json['name']
    price = request.json['price']
    description = request.json['description']

    product.name = name
    product.price = price
    product.description = description

    db.session.commit()

    return productSchema.jsonify(product)

@productsRoutes.route('/products/<id>', methods=['DELETE'])
def deleteProduct(id):
    product = Products.query.get(id) 
    db.session.delete(product) 
    db.session.commit()

    return productSchema.jsonify(product)  