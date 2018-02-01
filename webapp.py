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
    return render_template('home.html')
   
   

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))
@app.route('/q1')
def renderQuestion1():
    return render_template('question1.html',methods=['GET','POST'])
    
@app.route('/q2')
def renderQuestion2():
    return render_template('question2.html',methods=['GET','POST'])

@app.route('/q3')
def renderQuestion3():
    return render_template('question3.html',methods=['GET','POST'])
  
@app.route('/q4')
def renderQuestion4():
    return render_template('question4.html',methods=['GET','POST'])

@app.route('/q5')
def renderQuestion5():
    return render_template('question5.html',methods=['GET','POST'])

@app.route('/f1',methods=['GET','POST'])
def renderAnswer():
    return render_template('final.html',methods=['GET','POST'])

    
if __name__=="__main__":
    app.run(debug=True)
