from flask import Flask, render_template, request
app = Flask(__name__)
from covid import testData
from park import testData as park
from heart import testData_heart
from diabetes import testData_diabetes
from stroke import testData as stroke
import sqlite3
import smtplib

database=[]
@app.route("/Home")
def home():
    return render_template("index.html")

@app.route('/')
def index():

    return render_template('results.html')

@app.route('/covid')
def covid():
    return render_template('TESTYOURSELF.html')

@app.route('/parkinsons')
def parkinsons():
    return render_template('test_park.html')
    
@app.route('/heart')
def heart():
    return render_template('test_heart.html')

@app.route('/stroke')
def stroke():
    return render_template('test_stroke.html')

@app.route('/diabetes')
def diabetes():
    return render_template('test_diabetes.html')

@app.route('/sub', methods= ["POST"])
def sub():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = park(input_data)
        name="Parkinson's Disease"
        data=[name,result]
        return render_template('park_res.html',n = data)

@app.route('/sub_heart', methods= ["POST"])
def sub_heart():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = testData_heart(input_data)
        name="HEART ATATCK"
        data=[name,result]
        return render_template('park_res.html',n = data)
    
@app.route('/sub_diabetes', methods= ["POST"])
def sub_diabetes():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = testData_diabetes(input_data)
        name="Diabetes"
        data=[name,result]
        return render_template('park_res.html',n = data)

@app.route('/sub_stroke', methods= ["POST"])
def sub_stroke():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = stroke(input_data)
        name="STROKE"
        data=[name,result]
        return render_template('park_res.html',n = data)


@app.route('/results', methods= ["POST"])
def submit():
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        result = testData(input_data)
        name="COVID-19"
        data=[name,result]
        return render_template('park_res.html',n = data)

@app.route('/data_add', methods= ["POST"])
def result():
    conn=sqlite3.connect('data.db',check_same_thread=False)
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, test TEXT, result TEXT)")
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
    c.execute("INSERT INTO users VALUES (?,?,?,?)",input_data)
    #database.append([name,age,test,result])
    conn.commit()
    conn.close()
    return render_template('results.html')

@app.route('/data_show', methods= ["GET","POST"])
def show():
    conn=sqlite3.connect('data.db',check_same_thread=False)
    c=conn.cursor()
    c.execute("SELECT * FROM users")
    data=c.fetchall()
    return render_template('database.html',n = data)

@app.route('/delete_database', methods= ["POST"])
def delete():
    conn=sqlite3.connect('data.db',check_same_thread=False)
    c=conn.cursor()
    c.execute("DROP TABLE users")
    return render_template('results.html')

@app.route('/email_database', methods= ["POST"])
def email():
    conn=sqlite3.connect('data.db',check_same_thread=False)
    c=conn.cursor()
    c.execute("SELECT * FROM users")
    data=c.fetchall()
    if request.method == 'POST':
        input_dict = request.form
        input_data = tuple(input_dict.values())
        # Default email address and message
        from_email = "122abdulrahman@gmail.com"
        subject = "Test Email"
        message = data

        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, "passwords")

        # Send the email
        server.sendmail(from_email, input_data[0], f'Subject: {subject}\n\n{message}')
        server.quit()

if __name__ == '__main__':
    app.run()

