#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(f"{string}")
    return f'{string}'
    
    
    
@app.route('/count/<int:n>')
def count(n):
    # Generate a string with numbers from 0 to n, each on a new line using a list comprehension
    numbers = '\n'.join(str(num) for num in range(n)) + '\n'
    return numbers
    
    
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':  # 'div' instead of '/' to avoid URL issues
            if num2 == 0:
                return "Error: Division by zero", 400
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return "Error: Invalid operation", 400

        # Manually creating a JSON response string
        return f'{result}'

    except Exception as e:
        return f"Error: {str(e)}", 400