# Import Flask modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create an object named app
app = Flask(__name__)

# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXISTS users;'
users_table = """ 
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
data="""
INSERT INTO users 
VALUES
    ("Nurul Zudin", "nurulzudin@amazon.com"),
    ("Emrah", "emrah@google.com"),
    ("Mehmet", "mehmet@tesla.com")
"""
db.session.execute(drop_table)
db.session.execute(users_table)
db.session.execute(data)
db.session.commit()



# Write a function named `find_emails` which find emails using keyword from the user table in the db,
#  and returns result as tuples `(name, email)`.

def find_email(keyword):
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%';
    """
    result = db.session.execute(query)
    user_emails = [(row[0],row[1]) for row in result]

    if not any(user_emails):
        user_emails = [("Not Found", "Not FOUND")]
    return user_emails


# Write a function named `insert_email` which adds new email to users table the db.

def insert_email(name,email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}'
    """
    result = db.session.execute(query)
    response = ''
    data=f"""
    INSERT INTO users 
    VALUES
        ('{name}', '{email}'),
    """
    if name == None or email == None:
        response = "Name or Email is EMPTY!!!"
    elif not any(result):
        data=f"""
        INSERT INTO users 
        VALUES
        ('{name}', '{email}');
        """
        db.session.execute(data)
        db.session.commit()
        response = f"Name= {name} and email = {email} is added to db"
    else:
        response = f"there is a SAME {name} already too"
    return response

    

# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')
@app.route('/', methods = ['POST', 'GET'])
def emails():
    if request.method == 'POST':
        user_app_name = request.form['user_keyword']
        user_emails = find_email(user_app_name)
        return render_template("emails.html", show_result = True, keyword = user_app_name, name_emails = user_emails)
    else:
        return render_template("emails.html", show_result = False)

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')
@app.route("/add", methods = ['POST', 'GET'])
def addemail ():
    if request.method == 'POST':
        username=request.form["username"]
        useremail=request.form["useremail"]
        result_html = insert_email(username,useremail)
        return render_template("add-email.html",show_result=True, result_html=result_html)
    else:
        return render_template("add-email.html",show_result=False)

# Add a statement to run the Flask application which can be reached from any host on port 80.

if __name__ == "__main__":
    app.run(debug = True)
