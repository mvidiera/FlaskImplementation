#Jinja2 implemetation

'''
for statements or any condition {%  %}
Output printing {{    }}
Commenting {#.......#} in html page 
'''

#copying from integratingHTML.py

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')



@app.route('/success/<int:marks>') 
def success(score):
    res= " "
    if score>= 50:
        res= "PASS"
    else:
        res= "FAIL"
    return render_template('jinjaresult.html', result= res)
    

@app.route('/fail/<int:marks>') 
def fail(score):
    return "person has failed and the score is " + str(score) 

# result checker
@app.route('/results/<int:score>')
def results(marks):
    res= " "
    if marks< 50:
        res= 'Score is less than 50: Failed'
    else:
        res= 'Score is more than 50: Passed'

    return redirect(url_for(res, score=marks)) 


@app.route('/submit', methods=['POST','GET']) 
def submit():
    total_score= 0
    if request.method=="POST":
        science= float(request.form['science']) 
        ML= float(request.form['ML'])
        AI= float(request.form['AI'])
        NLP= float(request.form['NLP'])

        total_score= (science+ML+AI+NLP)/4

    res= " "
    if total_score>= 50:
        res= "success" 
    else:
        res= "fail"
   
    return redirect(url_for(res, score=total_score))


if __name__ == '__main__':
    app.run(debug=True)