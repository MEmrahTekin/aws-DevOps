# Import Flask modules
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

# Create an object named app
app = Flask(__name__)

# Configure sqlite database
app.config['MYSQL_DATABASE_HOST'] = 'database-1.cpx5vhrkiml2.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Clarusway_1'
app.config['MYSQL_DATABASE_DB'] = 'clarusway'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXISTS users;'
users_table = """
CREATE TABLE users (
  username varchar(50) NOT NULL,
  email varchar(50),
  PRIMARY KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
data="""
INSERT INTO users 
VALUES
    ("Nurul Zudin", "nurulzudin@amazon.com"),
    ("Emrah", "emrah@google.com"),
    ("Mehmet", "mehmet@tesla.com")
"""
cursor.execute(drop_table)
cursor.execute(users_table)
cursor.execute(data)



# Write a function named `find_emails` which find emails using keyword from the user table in the db,
#  and returns result as tuples `(name, email)`.

def find_email(keyword):
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%';
    """
    cursor.execute(query)
    result = cursor.fetchall(query)
    user_emails = [(row[0],row[1]) for row in result]

    if not any(user_emails):
        user_emails = [("Not Found", "Not FOUND")]
    return user_emails


# Write a function named `insert_email` which adds new email to users table the db.

def insert_email(name,email):
    query = f"""
    SELECT * FROM users WHERE username like '{name}'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    response = ''
    data=f"""
    INSERT INTO users 
    VALUES
        ('{name}', '{email}'),
    """
    if name == None or email == None:
        response = "Name or Email is EMPTY!!!"
    elif not any(result):
        cursor.execute(data)
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
    app.run(host='0.0.0.0', port=80)
