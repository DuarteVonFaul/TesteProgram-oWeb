from flask import render_template, request, jsonify
from models.product import Product
from models.buyer import Buyer
from . import to_dict

products = []
buyers = []
total_service_fee = 0

def init(app):
    @app.route('/sale')
    def sale():
        return render_template('questao_03.html')

    @app.route('/sale/buyers', methods=['GET'])
    def getBuyers():
        return jsonify(to_dict(buyers))

    @app.route('/sale/products', methods=['GET'])
    def getProducts():
        return jsonify(to_dict(products))

    @app.route('/sale/buyer/register', methods=['POST'])
    def registerBuyer():
        buyer_name = request.form.get('buyer')

        buyer = Buyer(buyer_name)
        buyers.append(buyer)

        return 'Buyer registered successfully'

    @app.route('/sale/buyer/addProduct', methods=['POST'])
    def buyerAddProduct():
        print(request.form.get('product_id'))
        buyer_id = int(request.form.get('buyer_id'))
        product_id = int(request.form.get('product_id'))

        if buyer_id < len(buyers) and product_id < len(products):
            buyer = buyers[buyer_id]
            product = products[product_id]
            buyer.addProduct(product)

            return 'Product added to buyer successfully'
        else:
            return 'Invalid buyer or product ID'

    @app.route('/sale/buyer/additional', methods=['POST'])
    def buyerAdditional():
        buyer_id = int(request.form.get('buyer_id'))

        if buyer_id < len(buyers):
            buyer = buyers[buyer_id]
            buyer.confirmAdditional()

            return 'Buyer additional confirmed successfully'
        else:
            return 'Invalid buyer ID'

    @app.route('/sale/product/register', methods=['POST'])
    def registerProduct():
        product_name = request.form.get('product')
        price = float(request.form.get('price'))

        product = Product(product_name, price)
        products.append(product)

        print(to_dict(products))

        return 'Product registered successfully'

    @app.route('/sale/calculate', methods=['POST'])
    def calculate():
        service_fee = 0
        json_buyers = []

        for product in products:
            count = 0
            list_buyers = []
            for buyer in buyers:
                if product in buyer.product:
                    count += 1
                    list_buyers.append(buyer)
            for buyer in list_buyers:
                buyer.price += float(product.price / count)

        for buyer in buyers:
            if buyer.addtional:
                buyer.valueAdditional += buyer.price * 0.1
            service_fee += buyer.price

        global total_service_fee
        total_service_fee += service_fee

        print(to_dict(buyers))

        return jsonify({'buyers': json_buyers, 'total_service_fee': round(total_service_fee, 2)})