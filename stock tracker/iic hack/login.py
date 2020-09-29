import os
import csv



from flask import Flask, render_template, request,session
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine,update,orm

"""id for the medicine table id=shop"""
shop=0




app=Flask(__name__)
"""key needed to run session in flask"""
app.secret_key = 'the secret key'
engine=create_engine('postgres://zrrzdqtlheepde:89cdf89f507190dc9bb3596cf4c0ac55993299eda8393dab4fd9666131bdd783@ec2-52-204-232-46.compute-1.amazonaws.com:5432/dbkdedb13nvri6')
db=scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("loginpage.html")

"""login mate nu"""
@app.route("/export",methods=["POST"])
def export():
    name=request.form.get("username")
    passw=request.form.get("password")
    login=db.execute("SELECT id,city,address,username,password from logins").fetchall()
    for lo in login:
        h=0;
        if( lo.username==name and lo.password==passw):
            h=1;
            session['a']=lo.id
            return render_template("upload.html")


    if(h==0):
            return render_template("error.html")

"""document upload karva mate"""
@app.route("/success" ,methods=["POST"])
def success():
    f=request.files['file']
    f.save(f.filename)
    g=open(f.filename)
    h=csv.reader(g)
    shopid=session.get('a',None)
    for mname, avail in h:
        db.execute("INSERT INTO medicines(mname,avail,shopid) VALUES (:mname,:avail,:shopid)",
        {"mname":mname,"avail":avail,'shopid':shopid})
        db.commit()
    return 'succeess'

"""registeration mate"""
@app.route("/exp", methods=["POST"])
def exp():
    city=request.form.get("shop")
    address=request.form.get("address")
    username= request.form.get("username")
    password= request.form.get("password")


    db.execute("INSERT INTO logins (city,address,username,password) VALUES (:city,:address,:username, :password)",
            {"city":city,"address":address,"username": username, "password": password})
    db.commit()
    return render_template("success.html")

"""new medicine add"""
@app.route("/add",methods=['POST'])
def add():
    mname=request.form.get("name")
    shopid=session.get('a',None)
    avail=request.form.get("1")
    if(avail==None):
        avail="NO"
    db.execute("INSERT INTO medicines(mname,avail,shopid) VALUES (:mname,:avail,:shopid)",
               {"mname":mname,"avail":avail,"shopid":shopid})
    db.commit()
    return "success"

"""update the medicine"""
@app.route("/update",methods=["POST"])
def updated():
    ame=request.form.get("name")
    hop=session.get("a",None)
    avail=request.form.get("1")
    med=Medicine.query.filter_by(mname=ame).first()
    print(med)
    return "success"

"""serch page mate"""
@app.route("/serc",methods=["POST"])
def serc():
    med=db.execute("SELECT avail,mname,shopid FROM medicines ").fetchall()
    log=db.execute("SELECT id,username,address,city FROM logins").fetchall()
    cit=request.form.get("city")
    mname=request.form.get("medicine")
    a=[]
    for medicine in med:
        if medicine.mname==mname and (medicine.avail=="yes" or medicine.avail=="YES"):
            a.append(medicine.shopid)

    b=[]
    for login in log:
        for i in a:
            if login.id == i:
                if login.city == cit:
                    b.append(login.id)


    return render_template("search2.html",b=b,log=log)


@app.route("/search.html")
def search():
    return render_template("search.html")
@app.route("/loginpage.html")
def login():
    return render_template("loginpage.html")
@app.route("/update.html")
def update():
    return render_template("update.html")
@app.route("/new.html")
def new():
    return render_template("new.html")
@app.route("/registerpage.html")
def hindex():
    return render_template("registerpage.html")


app.run()

