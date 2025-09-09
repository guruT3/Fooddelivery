from  flask import Flask,redirect,render_template,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm,SignupForm,FeedbackForm,DeliveryInfo,Checkout
from Products import foods
from  datetime import datetime
from flask_migrate import Migrate



app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///storage.db'
db=SQLAlchemy(app)

migrate = Migrate(app, db)

class Storage(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  phone_number= db.Column(db.String(100), nullable=False)
  password= db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f"Storage('{self.name}', '{self.email}', '{self.phone_number}', '{self.password}')"

with app.app_context():
  db.create_all()



@app.route("/")
def home():
  return render_template('home.html',title="welcome to Gamma")


@app.route("/signup",methods=["GET","POST"])
def signup():
  form=SignupForm()
  if form.validate_on_submit():
    new_usr = Storage(
    name=form.name.data,
    email=form.email.data,
    password=form.password.data,
    phone_number=form.phone_number.data
)

    db.session.add(new_usr)
    db.session.commit()
    return redirect(url_for("login"))
  return render_template("signup.html",title="Signup Page",form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Storage.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            return redirect(url_for("products"))
          
        else:
            flash("Invalid email or password")
    return render_template("login.html", title="Login Page", form=form)

@app.route("/shopnow")
def shopnow():
  return redirect(url_for("login"))
    
@app.route("/products",methods=["GET"])
def products():
  return  render_template("products.html",title="All Products",foods=foods)

@app.route("/ordernow")
def ordernow():
  return redirect(url_for("deliveryinfo"))

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)  
  email = db.Column(db.String(100), nullable=False)
  phone_number = db.Column(db.String(100), nullable=False)
  address = db.Column(db.String(100), nullable=False)
  pincode = db.Column(db.String(100), nullable=False)
  order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return f"Storage('{self.name}', '{self.email}', '{self.phone_number}', '{self.address}', '{self.pincode}', '{self.order_date}')"




@app.route("/deliveryinfo",methods=["GET","POST"])
def deliveryinfo():
  form=DeliveryInfo()
  if form.validate_on_submit():
    new_order=Order(name=form.name.data,email=form.email.data,phone_number=form.phone_number.data,address=form.address.data, pincode=form.pincode.data)
    db.session.add(new_order)
    db.session.commit()
    flash(f"Order Placed")
    return redirect(url_for("payment"))
  return render_template("deliveryinfo.html",title="Delivery Info",form=form)
  
   
@app.route("/payment",methods=["GET","POST"])
def payment():
  forms=Checkout()
  if forms.validate_on_submit():
    flash(f"Payment Successful")
    return redirect(url_for("ordersuccess"))
  return render_template("payment.html",title="Payment Page",forms=forms)

@app.route("/food/<food_id>")
def food_detail(food_id):
  food=foods.get(food_id)
  if  food:
    return render_template("food_details.html",title="hii",food=food)
  else:
    flash(f"not found")
    return redirect(url_for("products"))
  
@app.route("/ContactUs")
def ContactUs():
  return render_template("ContactUs.html")


@app.route("/ordersuccess")
def ordersuccess():
  return render_template("ordersuccess.html")








if __name__=="__main__":
  app.run(debug=True)