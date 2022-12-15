# Redirecting to different URL for different result 
# url_for

#import redirect and url_for package 

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my first page"

#success 

@app.route('/success/<int:marks>') 
def success(score):
    return "person has passed and the score is " + str(score)
    # or html 
    # return "<html><body><h1> The result is passed </h1></body></html>" not good approach
    

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

if __name__ == '__main__':
    app.run(debug=True)

    #op: person has passed and the score is " + str(score)