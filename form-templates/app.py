### building url dinamically

from flask import Flask ,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/sucess/<int:score>')
def sucess(score):
    return 'the person has passed and marks is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and marks is ' + str(score)
    return "<html><body><h1>This is result only<h1><body><html>"
    
## redirect page

@app.route('/results/<int:marks>')
def results(marks):
    result =""
    if marks < 50:
        result ="fail"
    else:
        result ="sucess"
    return redirect(url_for(result , score=marks ))

if __name__ == "__main__":
    app.run(debug=True)
