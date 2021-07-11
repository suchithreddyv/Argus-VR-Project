
#Back-end program for registration form ,to store details in GCP through Flask


import pymysql,re,tkinter
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
    if request.method=='POST' :
       
        name=request.form['name']
        email=request.form['email']
        mob=request.form['mobile']
        password=request.form['password']
        retypepassword=request.form['cpassword']
        #Code to validate and insert users into the database
        
        npattern="^[a-zA-Z\s\.]+$"
        epattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
        mpattern="[7-9]{1}[0-9]{9}"
        ppattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"

        if(re.match(npattern,name) and re.match(epattern,email) and re.match(mpattern,mob) and re.match(ppattern,password) and password==retypepassword):

            with db.connect() as conn:
            # Execute the query and fetch all results
                conn.execute("insert into registration (emailid,password,retype_password,Name,Mobileno) values(%s,%s,%s,%s,%s)" ,(email,password,retypepassword,name,mob))
                conn.execute("insert into login (emailid,password) values(%s,%s)" ,(email,password))
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

    