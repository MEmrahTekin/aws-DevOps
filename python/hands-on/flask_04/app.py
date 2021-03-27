from flask import Flask
from flask.globals import request
from flask.templating import render_template

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/total", methods=["GET","POST"])
def total():
    if request.method == "POST":
        value1=request.form.get("value1")
        value2=request.form.get("value2")
        value3=request.form["value3"]
        return render_template("number.html", total = int(value1)+int(value2)+int(value3))
    else:
        return   render_template("number.html")



if __name__ == "__main__":
    app.run(debug=True)