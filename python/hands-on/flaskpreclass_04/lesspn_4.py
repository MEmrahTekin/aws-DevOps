from flask import Flask, redirect,render_template,request
app = Flask (__name__)

@app.route("/")
def home(name="Emrah"):
    return render_template("index.html" , name=name)

@app.route("/greet",methods=['GET'])
def greet() :
    if not request.query_string :
        return render_template("greet.html" , user='Send your user name with "user" param in query string')
    user = request.args.get("user")
    return render_template("greet.html" , user=user)

@app.route("/login",methods=["GET","POST"])
def login ():
    if request.method=="POST":

        username = request.form.get("username")
        password = request.form["password"]
        if password == "clarusway":
            return render_template("secure.html",user=username)
        else:
            return render_template("login.html",control=1,user=username)

    return render_template("login.html")

    

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=80)