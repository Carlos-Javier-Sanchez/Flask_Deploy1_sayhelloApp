from flask import Flask, render_template, render_template_string, request, flash
# set a Class
app= Flask(__name__)
#set Secret Key (never show up a secrete key)
app.secret_key="thx1138thx1138"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

#handling greet button - Fetch user input 
@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!" )
    return render_template("index.html")
