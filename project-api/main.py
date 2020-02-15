from flask import Flask, jsonify, request
import jsonpickle
import sqlite3
from flask import g

DATABASE = '/Users/serdar/Documents/GitHub/flask-examples/project-api/my_project.db'
app = Flask(__name__)
conn = sqlite3.connect('my_project.db')
print("Connected")


class Product:
    def __init__(self,id,name,price):
        self.id = id        
        self.name = name
        self.price = price #TODO: Consider changing properties to private

classProducts = {
    231: Product(231,'A',1000),
    232: Product(232,'B',1001),
    233: Product(233,'C',1002) 
}

@app.route('/products', methods=['GET'])
def returnAllProducts():
    app.logger.warning("Return all products")
    response = app.response_class(
        response=jsonpickle.encode(classProducts, unpicklable=False),
        status=200,
        mimetype='application/json'
    )
    cursor = conn.execute("SELECT * from products")
    for row in cursor:
        print(row)
    conn.close()
    return response

print(returnAllProducts())

@app.route('/products/<int:productId>', methods=['GET'])
def returnProducts(productId):
    if not productId in classProducts:
        return jsonify(), 404

    product = classProducts[productId]
    response = app.response_class(
        response=jsonpickle.encode(product, unpicklable=False),
        status=200,
        mimetype='application/json'
    )
    
    return response

@app.route('/products', methods=['POST'])
def createNewProduct():
    product = request.get_json()

    productId = product['id']
    classProducts[productId] = Product(product['id'],product['name'],product['price'])
    app.logger.warning("new product created")
    
    return jsonify(product), 201

@app.route('/products/<int:productId>', methods = ['DELETE'])
def deleteProduct(productId):
    if not productId in classProducts: 
        return jsonify(), 404

    del classProducts[productId]
    return jsonify(), 204

@app.route('/products/<int:productId>', methods = ['PUT'])
def putProduct(productId):
    product = request.get_json()
    updatedProduct = Product(productId, product['name'], product['price'])
    classProducts[productId] = updatedProduct
    response = app.response_class(
        response=jsonpickle.encode(updatedProduct, unpicklable=False),
        status=200,
        mimetype='application/json'
    )
    return response, 200

@app.route('/products')
def queryString():
    arg1 = request.args['category']
    arg2 = request.args['brand']

    return 'Filter; Category:' + arg1 + 'Brand:' + arg2
