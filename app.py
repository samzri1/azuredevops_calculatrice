from flask import Flask, render_template, request

app = Flask(__name__)

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: division par zéro!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    choix = request.form['operation']

    if choix == "addition":
        result = addition(num1, num2)
        operation = "+"
    elif choix == "soustraction":
        result = soustraction(num1, num2)
        operation = "-"
    elif choix == "multiplication":
        result = multiplication(num1, num2)
        operation = "*"
    elif choix == "division":
        result = division(num1, num2)
        operation = "/"

    return render_template('result.html', num1=num1, num2=num2, operation=operation, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

