# server/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    View for the base URL (/).
    Displays the title of the application.
    """
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    """
    View for printing a string.
    Prints the string to the console and displays it in the browser.

    Args:
        text (str): The string to print and display.
    """
    print(text)  # Print to the console
    return f'<p>{text}</p>'  # Display in the browser

@app.route('/count/<int:number>')
def count(number):
    """
    View for displaying numbers in a range.
    Displays all numbers from 0 up to (but not including) the given number,
    each on a new line.

    Args:
        number (int): The upper bound of the range (exclusive).
    """
    if number < 0:
        return "<p>Number must be non-negative.</p>"
    
    output = ""
    for i in range(number):
        output += f'<p>{i}</p>'  # Build the output string
    return output

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    """
    View for performing math operations.
    Performs the specified operation on two numbers.

    Args:
        num1 (int): The first number.
        operation (str): The operation to perform (+, -, *, div, %).
        num2 (int): The second number.
    """
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return '<p>Cannot divide by zero.</p>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Invalid operation.  Use +, -, *, div, or %.</p>'

    return f'<p>{num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
