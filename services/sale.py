
from flask import request, render_template


class Calculator:
    def __init__(self):
        self.items = []
        self.total_service_fee = 0

    def calculate_service_fee(self, client, price):
        client = request.form.get('client')
        product = request.form.get('product')
        price = float(request.form.get('price'))

        service_fee = 0

        # Verificar se o cliente deve pagar taxa de serviço
        if client in [item['client'] for item in self.items]:
            service_fee = price * 0.1

        self.items.append({
            'client': client,
            'product': product,
            'price': price,
            'service_fee': round(service_fee, 2)
        })

        self.total_service_fee += service_fee

        return render_template('table.html', items=self.items, total_service_fee=round(self.total_service_fee, 2))

calculator = Calculator()