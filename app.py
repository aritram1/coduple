from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('_template.html')

@app.route('/user')
def user():
    # return 'Hello from User page'
    return render_template('Userhome.html')

@app.route('/user/<userId>')
def userdetails(userId):
    # user = SELECT User from User where id = userId
    user = {'id' : 1, 'firstname' : 'Aritra', 'location' : 'Arendal'}
    return render_template('Userdetail.html', user = user)

if __name__  ==  '__main__':
    app.run(debug = True)