# to build dynamic URL

from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my first page"

#success 

@app.route('/success/<int:score>') # here int score is called variable rules
def success(score):
    return "person has passed and the score is " + str(score) #score is int and to concatenate within
    # im converting str(score) and adding to that sentence

@app.route('/fail/<int:score>') 
def fail(score):
    return "person has failed and the score is " + str(score) 

# result checker
@app.route('/results/<int:score>')
def results(score):
    res= " "
    if score< 50:
        res= 'Score is less than 50: Failed'
    else:
        res= 'Score is more than 50: Passed'
#when I run webpage with /results/60, OP: Score is more than 50: Passed
#  /results/35, OP: Score is less than 50: Failed
    return res
# to display different webpage for pass and failed: check urlfor.py
if __name__ == '__main__':
    app.run(debug=True)