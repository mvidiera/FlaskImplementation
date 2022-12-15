#integrating HTMl with flask. Jinja 2 
#HTTP verb: GET and POST

from flask import Flask, redirect, url_for, render_template, request
# to use render_template, create folder template and a file within that called 
#request helps to read posted value

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html') #rather than return stamtement, use return render call index.html within render_temp()
#this fuction looks for folder called templates and then looks for the file mentioned inside function
#success 


# in result checker, I will create new HTML file for each result: pass or fail
# Rather than entering marks in link, lets create a new html file

@app.route('/success/<int:marks>') 
def success(score):
    res= " "
    if score>= 50:
        res= "PASS"
    else:
        res= "FAIL"
    return render_template('result.html', result= res)
    

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
#instead of return res, 
    return redirect(url_for(res, score=marks)) #url_for: 1st parameter is page(res) and then send score 

#After result checker is submitted this html page is generated
#result checker html page

@app.route('/submit', methods=['POST','GET']) #methods can be post or get
def submit():
    total_score= 0
    if request.method=="POST":
        science= float(request.form['science']) #default value is string, convert into float to cal avg 
        ML= float(request.form['ML'])
        AI= float(request.form['AI'])
        NLP= float(request.form['NLP'])

        total_score= (science+ML+AI+NLP)/4

    res= " "
    if total_score>= 50:
        res= "success" #redirect this to success page
    else:
        res= "fail"
    #build URL: dynamic url generation
    return redirect(url_for(res, score=total_score))


if __name__ == '__main__':
    app.run(debug=True)