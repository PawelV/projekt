#from flaskext.mysql import MySQL
from flask import Flask, render_template, json, request
app = Flask(__name__)
#mysql = MySQL()

config = {
        'user': 'root',
        'password': 'pawelp',
        'host': 'db',
        'port': '3306',
        'database': 'BucketList'
    }
connection = mysql.connector.connect(**config)
 
# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'jay'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
#app.config['MYSQL_DATABASE_DB'] = 'BucketList'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

#conn = mysql.connect()
#cursor = conn.cursor()

@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route("/")
def main ():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#from werkzeug import generate_password_hash, check_password_hash
#cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
#_hashed_password = generate_password_hash(_password)

#data = cursor.fetchall()
#if len(data) is 0:
#    conn.commit()
#    def foo(): return json.dumps({'message':'User created successfully !'})
#else:
#    def foo(): return json.dumps({'error':str(data[0])})

if __name__ == "__main__":
	app.run()