from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float

app = Flask(__name__)  # create the instance of the flask class


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculate():
    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

'''
1 (a)Write the Circle class (with the perimeter and area methods) in a separate 
python module (like helper.py, in the repository) called circle.py and import it into
the main flask module.
'''
from circle import Circle
@app.route('/circle', methods=['GET', 'POST'])  # associating GET and POST methods with this route
def circle_calculator():
    if request.method == 'POST':
        # get the radius value and the chosen operation from the form
        radius = request.form['radius']
        operation = request.form['operation']

        # make sure the operation is valid (useful even if dropdown is used)
        if operation not in ['perimeter', 'area']:
            return render_template('circle.html',
                                   result='Operation must be either "perimeter" or "area".')

        try:
            # convert the radius to a float
            radius = convert_to_float(value=radius)
        except ValueError:
            # if conversion fails (e.g., user enters text), show an error message
            return render_template('circle.html',
                                   result="Invalid input. Please enter a valid number for radius.")

        try:
            # create a Circle object with the provided radius
            circle = Circle(radius=radius)

            # perform the selected operation
            if operation == 'perimeter':
                calc_result = circle.perimeter()
            else:
                calc_result = circle.area()

            # return the result as a string to the template
            return render_template('circle.html', result=f"{operation.capitalize()}: {calc_result:.2f}")

        except Exception as e:
            # catch any unexpected errors and return a generic message
            return render_template('circle.html', result="An error occurred: " + str(e))

    # render the form when the page is accessed via GET
    return render_template('circle.html')



