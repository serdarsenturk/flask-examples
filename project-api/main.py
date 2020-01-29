from flask import Flask, jsonify, request

app = Flask(__name__)

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
    return jsonify(products)


@app.route('/products', methods=['POST'])
def createNewProduct():
    product = request.get_json()

    # products is a dictionary. A dictionary records contains a Key and a Value
    # in that case your record only has Value

    # what is the Key for this new record?

    # Once bunu cevapla:: what is the output of the GET /products call after you add new product?
    # okumuyordum burayı.whatsapp dan yaz

    productId = product[id]
    products[productId] = product
    app.logger.warning("new product created")
    return jsonify(product)

@app.route('/products/<int:productId>', methods = ['DELETE'])
def deleteProduct(productId):
    # consider getting productId from the url.
    # see : http://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
    del products[productId]
    return jsonify(products)

@app.route('/products')
def queryString():
    arg1 = request.args['category']
    arg2 = request.args['brand']

    return 'Filter:' + arg1 + 'Brand:' + arg2