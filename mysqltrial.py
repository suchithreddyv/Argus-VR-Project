
#Back-end Program for Contact Form to add details to GCP through Flask

import pymysql
import re,tkinter
from tkinter import messagebox
from flask import Flask,render_template,request,redirect,flash,url_for
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:tiger@127.0.0.1/test')
db=engine
votes=[]
app=Flask(__name__)
app.secret_key = 'mysecretkey'
message=""

@app.route('/',methods=['POST','GET'])
def index():
    global message
    if request.method=='POST':
        
        name=request.form['name']
        email=request.form['email']
        mob=request.form['number']
        mes=request.form['message']

        #regular expressions for validaions
        npattern="^[a-zA-Z\s\.]+$"
        epattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
        spattern="[7-9]{1}[0-9]{9}"

        if(re.match(npattern,name) and re.match(epattern,email) and re.match(spattern,mob)):
            with db.connect() as conn:
            # Execute the query and insert results
                conn.execute("insert into contact (Name,Email,Mobileno,Message) values(%s,%s,%s,%s)" ,(name,email,mob,mes))
                message="The user  added successfully"
                return redirect('/')
        else :
            root=tkinter.Tk()
            root.withdraw()
            messagebox.showerror("ERROR","Enter Valid Credentials")
            return redirect(url_for('index'))
    else:
        return render_template('index.html',message=message)

if __name__=="__main__":
    app.run(debug=True)

    