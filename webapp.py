import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                    #The value should be set in Heroku (Settings->Config Vars).

@app.route('/')
def renderMain():
    session['correct'] = 0
    print(session['correct'])
    return render_template('home.html')


@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))
@app.route('/q1',methods=['GET','POST'])
def renderQuestion1():
    return render_template('question1.html')

@app.route('/q2',methods=['GET','POST'])
def renderQuestion2():
    if 'Quartz' == request.form["a"]:
        session['correct'] += 1 
    return render_template('question2.html')
 
@app.route('/q3',methods=['GET','POST'])
def renderQuestion3():
    if 'Magnetism' == request.form["b"]:
        session['correct'] += 1 
    return render_template('question3.html')

@app.route('/q4',methods=['GET','POST'])
def renderQuestion4():
    if 'Calcite' == request.form["c"]:
        session['correct'] += 1     
    return render_template('question4.html')

@app.route('/q5',methods=['GET','POST'])
def renderQuestion5():
    if 'Talc' == request.form["d"]:
        session['correct'] += 1 
    return render_template('question5.html')

@app.route('/f1',methods=['GET','POST'])
def renderAnswer():
    if '10' == request.form["e"]:
        session['correct'] += 1     
    for key in session:
        print(session[key])
    return render_template('final.html', correct = session['correct'] )
    
    
if __name__=="__main__":
    app.run(debug=True)
