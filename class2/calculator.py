from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
   """ Displays the index page accessible at '/' """

   return render_template('index.html')

@app.route('/answer/', methods=['POST'])
def answer():
    """Route where we send calculator form input"""

    error = None
    result = None

    num = request.form['num']  
    num2 = request.form['num2']
    operation = request.form['operation']

    try:
        x = float(num)
        y = float(num2)

        if operation == "+":
            result = x + y

        elif operation == "-":
            result = x - y

        elif operation == "/":
            result = x / y

        elif operation == "*":
            result = x * y

        else:
            operation = "%"
            result = x % y

        return render_template(
            'index.html',
            num=num,
            num2=num2,
            operation=operation,
            result=result,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            num=num,
            num2=num2,
            operation=operation,
            result="Invalid Input",
            calculation_success=False,
            error="Undefined - division by zero"
        )
        
    except ValueError:
        return render_template(
            'index.html',
            num=x,
            num2=y,
            operation=operation,
            result="Invalid Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

if __name__=="__main__":
    app.run(debug=True) 

