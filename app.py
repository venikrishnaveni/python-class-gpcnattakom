from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return "Welcome to my home page"

@app.route("/contacts")
def contact():
    return "welcome to contacts"

@app.route("/about")
def about():
    return "welcome to about"



if(__name__=="__main__"):
    app.run(debug=True)
