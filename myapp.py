from flask import Flask, request, render_template, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
from flask_mail import Mail, Message

app = Flask(__name__)

Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"
class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    subject = StringField("Subject",validators = [DataRequired()])
    message = TextAreaField("Message",validators = [DataRequired()])
    submit = SubmitField(label="Submit")

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'dmitry.v.bandurin@gmail.com'
app.config["MAIL_PASSWORD"] = 'pkjqxjhbnwngklvo'
mail.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('Index called')
    return render_template('home_product.html')

@app.route("/pred_repair", methods=['GET', 'POST'])
def pred_repair():
    print('Solutions called, request.method = ',request.method)
    return render_template('predictive_repair.html')

@app.route("/supply_chain", methods=['GET', 'POST'])
def supply_chain():
    print('Solutions called, request.method = ',request.method)
    return render_template('supply_chain.html')

@app.route("/logistics", methods=['GET', 'POST'])
def logistics():
    print('Solutions called, request.method = ',request.method)
    return render_template('logistics.html')

@app.route("/iiot", methods=['GET', 'POST'])
def iiot():
    print('Solutions called, request.method = ',request.method)
    return render_template('iiot.html')

@app.route("/pipelines", methods=['GET', 'POST'])
def pipelines():
    print('Solutions called, request.method = ',request.method)
    return render_template('pipelines.html')

@app.route("/dashboards", methods=['GET', 'POST'])
def dashboards():
    print('Solutions called, request.method = ',request.method)
    return render_template('dashboards.html')

@app.route("/blogs", methods=['GET', 'POST'])
def blogs():
    return render_template('blogs.html')

@app.route("/about_us", methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html')

@app.route("/our_projects", methods=['GET', 'POST'])
def our_projects():
    return render_template('our_projects.html')

#https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
@app.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
  form=contactForm()
  if form.validate_on_submit():
        print(f"Name:{form.name.data}, E-mail:{form.email.data}, message:{form.message.data}")
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:    
      #send this email to us
      msg = Message(form.subject.data, sender=form.email.data, recipients=['dmitry.v.bandurin@gmail.com'])
      msg.body = """  
      From: %s <%s>  
           %s  
      """ % (form.name.data, form.email.data, form.message.data)
      
      print(msg)
    
      mail.send(msg)

      return 'Thank you! We will contact you soon.'
    
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
  

# @app.route("/document", methods=['GET', 'POST'])
# def document():
#     print('Documents called, request.method = ',request.method)
#     return render_template('document.html')

# @app.route("/ecom", methods=['GET', 'POST'])
# def ecom():
#     print('ECom called, request.method = ',request.method)
#     return render_template('ecom.html')

if __name__ == '__main__':
    app.run(port=5003, debug=True)
