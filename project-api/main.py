from flask import Flask, jsonify, request
import jsonpickle

app = Flask(__name__)

class Product:
    def __init__(self,name,id,price):
        self.name = name
        self.id = id
        self.price = price #TODO: Consider changing properties to private

classProducts = {1:Product}

products = {
    231 : {
        'id' : 231,
        'name' : 'A',
        'price' : 1000
    }, 
    232 : {
        'id' : 232,
        'name' : 'B',
        'price' : 1001
    },
    233 : {
        'id' : 233,
        'name' : "C",
        'price' : 1002
    }
}

@app.route('/products', methods=['GET'])
def returnAllProducts():
    app.logger.warning("Return all products")
    return jsonpickle.encode(classProducts)


@app.route('/products', methods=['POST'])
def createNewProduct():
    product = request.get_json()

    productId = product['id']
    classProducts[productId] = Product(product['id'],product['name'],product['price'])
    app.logger.warning("new product created")
    
    return jsonify(product)

@app.route('/products/<int:productId>', methods = ['DELETE'])
def deleteProduct(productId):
    # consider getting productId from the url.
    # see : http://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
    del classProducts[productId]
    return jsonify(classProducts)

@app.route('/products')
def queryString():
    arg1 = request.args['category']
    arg2 = request.args['brand']

    return 'Filter:' + arg1 + 'Brand:' + arg2

@app.route('/products/<int:productId>', methods = ['PUT'])
def putProduct(productId):
    product = request.get_json()
    classProducts[productId] = Product(product['id'],product['name'],product['price'])
    return jsonpickle.encode(classProducts)
