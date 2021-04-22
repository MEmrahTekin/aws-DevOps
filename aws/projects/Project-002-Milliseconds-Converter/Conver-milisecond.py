from flask import Flask,redirect, render_template, request

app = Flask(__name__)

def result(number):
    if int(number) < 1000:
        result= f"just {number} millisecond/s"
        return result
    else:
        number = int(number)
        hour = number // (3600000)
        number%=3600000
        minute = number // (60000)
        number%=60000       
        second = number // (1000)
        result =  (hour>0)*(str(hour)+ " hour/s ") +  (minute>0)*(str(minute) +" minute/s ")+ (second>0)* (str(second) + " second/s")
        return result        


@app.route("/",methods=["GET","POST"])
def index():
    if request.method== "POST":
        number = request.form.get("number")
        if number.isdecimal() == False:
            return render_template("index.html",not_valid = True, developer_name="EmRaH")
        else:
            return render_template("result.html",milisecond = number, result = result(number), developer_name="EmRaH")
    else:
        return render_template("index.html",not_valid = False, developer_name="EmRaH")




if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=80)
