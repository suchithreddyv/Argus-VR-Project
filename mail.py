

# Program to send mails through flask


from flask import Flask,render_template,request
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='suchithreddyvemula@gmail.com'
app.config['MAIL_PASSWORD']='vsr30822'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)

@app.route('/')
def index():
    return render_template("mail.html")

@app.route('/sendmail',methods=['GET','POST'])
def sendmail():     #method to send mails automatically
    global disp
    if request.method == "POST":
        em = request.form['email']
        mes=Message(body='Hello there this is test mail',subject='Test Video Link -Team Argus',sender='suchithreddyvemula@gmail.com',recipients=[em])
        mail.send(mes)
        disp='Mail sent !'
        return render_template('mail.html',message=disp)

if __name__ == "__main__":
    app.run(debug=True)