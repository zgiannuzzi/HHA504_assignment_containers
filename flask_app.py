from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

#@app.route('/')
#def hello_world():
    #return 'Hello, World! From a Flask app in a Docker container!'


@app.route('/', methods=['GET','POST'])
def hello_world():
    print('success')
    return render_template('login.html', var_home = url_for('rand_number'),var_home2 = url_for('hello_world'))
    
@app.route('/home', methods = ['GET', 'POST'])
def rand_number():
    random_number = random.randint(1, 100)
    print(random_number)
    return render_template("index.html",number=random_number,var_home2 = url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')