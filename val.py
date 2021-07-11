
# Back-end Program for Login Form - To check login credentials from google cloud sql,validate them 


import pymysql
import re,tkinter
from tkinter import messagebox
from flask import Flask,flash,render_template,request,redirect,url_for
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:tiger@127.0.0.1/test')
db=engine
votes=[]
app=Flask(__name__)
app.secret_key = 'mysecretkey'

message=""

@app.route('/',methods=['POST','GET'])
def index():                 # Method to read the data & validate them
    global message
    if request.method=='POST':
       
        username=request.form['email']
        password=request.form['password']

        ppattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"      #regular expressions for validations
        upattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
        if(re.match(upattern,username) and re.match(ppattern,password)):
            print("username & password are valid")
            with db.connect() as conn:
            # Execute the query and fetch all results
                recent_votes = conn.execute("select * from login where emailid=%s",(username))
                for i in recent_votes:
                    votes.append(i[1])

                if(len(votes)):                 
                    print(votes)
                    if(votes[0]==password):
                        message="User login Successfull"
                        return redirect('/')
                    else:
                        message="User login UnSuccessfull"
                        return redirect('/')
                else:
                    message="User doesn't exist Please register "
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

    