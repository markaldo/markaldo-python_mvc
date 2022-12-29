from unicodedata import name
from flask import Flask, render_template, request

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/details/', methods=['POST'])
def details():

    error = None
    result = None

    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    
    try:
        input1 = (first_input)
        input2 = float(second_input)

        if  input2 < 50000:
            result = 3

        else:
            result = 4

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            result=result,
            data_correct=True 
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            result="Invalid Input",
            data_correct=False,
            error="Recheck the data you have entered"
        )

@Flask_App.route('/details2/', methods=['POST'])
def details2():

    reply = None
    
    specialization = request.form['specialization']

    if  specialization == "WDA":
                reply = 2

    else:
                reply = 7

    return render_template(
            'base.html',
            specialization=specialization,
            reply=reply,
        )

@Flask_App.route('/details3/', methods=['POST'])
def details3():

    modules = request.form['sub']
    #first_input=name
    return render_template(
            'fresh.html',
            #name = name,
            modules=modules,
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()