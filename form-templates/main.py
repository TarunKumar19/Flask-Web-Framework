## integrate HTml with Flask    
## HTTP verb   Get and Post


from flask import Flask ,redirect,url_for,render_template,request
### building url dinamically

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    res=""
    if score >=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('rest.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and marks is ' + str(score)
    
## redirect page

# @app.route('/results/<int:marks>')
# def results(marks):
#     result =""
#     if marks < 50:
#         result ="fail"
#     else:
#         result ="sucess"
#     return redirect(url_for(result , score=marks ))

## read posted value from html

@app.route('/submit',methods= ['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form ['science'])
        maths=float(request.form ['maths'])

        total_score = (science + maths)/2
    
    res=""  
    if total_score >= 50:
        res="sucess"
    else:
        res="fail"
    return redirect(url_for(res, score=total_score))

   

if __name__ == "__main__":
    app.run(debug=True)

   