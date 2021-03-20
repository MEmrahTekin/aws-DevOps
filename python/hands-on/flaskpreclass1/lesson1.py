from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

@app.route("/about")
def about ():
    return "<h1> This is my about page</h1>"

@app.route("/error")
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>' 

@app.route("/hello")
def hello():
    return '<h1>Hello, World! </h1>'

@app.route("/admin")
def admin():
    return redirect ("/error")

@app.route("/<string:name>")
def greet(name):
    return render_template("greet.html",name =name)

@app.route('/greet-admin')
def greet_admin(param="Masteradminn!!"):
    return redirect("/hello",param)

@app.route('/list10')
def list10():
    return render_template("list10.html")

@app.route("/evens")
def evens():
    return render_template("evens.html")




if __name__ == "__main__":
    app.run(debug = True)