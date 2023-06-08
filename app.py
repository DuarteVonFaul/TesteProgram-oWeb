from flask import Flask, render_template, request
from services.calc import arabic_to_roman, roman_to_arabic
from resources.gameOfLifeResources import init as GameOfLife
from resources.saleResources import init as Sale

app = Flask(__name__)



@app.route('/calc', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        number = request.form['number']
        converted_number = ''

        if number.isnumeric():
            try:
                converted_number = arabic_to_roman(int(number))
            except ValueError as e:
                converted_number = str(e)
        else:
            try:
                converted_number = roman_to_arabic(number.upper())
            except ValueError as e:
                converted_number = str(e)

        return render_template('questao_01.html', number=number, converted_number=converted_number)
    else:
        return render_template('questao_01.html')
    

GameOfLife(app)
Sale(app)
    

if __name__ == '__main__':
    app.run(debug=True)