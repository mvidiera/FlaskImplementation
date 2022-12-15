from flask import Flask

# 1. WSGI application: communicates btw web server and web app
app = Flask(__name__) #app is the object of flask. this acts as WSGI app

#2. decorator: 
@app.route('/')  #decorator: 2 parameters: rules and option. rule is string: url. 
#/ means no specific url and root home page

#3. function is defined beneath decorator, it means this function will be executed after the decorator
def welcome():
    return "This is my first Flask project, This is second sentence which is modified to check how changes are made"
#trying out more functions

@app.route('/hellomsg')#function names should be different though it has different routes, it shouldnt be same
def hellomsg():
    return "This is my second page or exentension /hellomsg"

#main()
if __name__== '__main__': #starting point of pgm execution -> this goes to line 3
    app.run(debug=True)

    # second sentence in return will not execute even if I quit and execute again. 
    # to make this Im adding one parameter into run() ie debug= True
    
# NOTE: debugging was running, any changes made like debug= True, second sentence 
# also hellomsg() wasnt working. 
# make sure debugging is off (stopped) on top there shouldnt be any window for debugging