from flask import Flask,render_template,redirect, request


app = Flask(__name__)

def format(value):
    if not value.isdecimal() or  not ( 0 < int(value) < 4000 ):
        return True

def roman(value):
    dicti = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50,"XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
    value = int(value)
    result=""
    while value != 0:
        for i in dicti:
            result+=i*(value//dicti[i])
            value%=dicti[i]
    return result

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        value=request.form.get("number")
        if format(value):
            return render_template("index.html",not_valid=True)
        else:
            return render_template("result.html",number_roman=roman(value),number_decimal=value)
    else: 
        return render_template("index.html",not_valid=False)



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=80)

