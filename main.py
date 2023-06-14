from flask import Flask, render_template
from forms import ContactForm
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

#Get user info to send email
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
my_email= os.getenv("MY_EMAIL")
api_key_gmail = os.getenv("APP_PASSWORD_GMAIL")


app = Flask(__name__)
app.config["SECRET_KEY"]= "myPass1234!!"

@app.route('/', methods=["GET", "POST"])
def home():
    form_python = ContactForm()

    if form_python.validate_on_submit():
        user_name = form_python.name.data
        user_email = form_python.email.data
        user_subject = form_python.subject.data
        user_message = form_python.message.data

        user_info = {
            "name": user_name,
            "email": user_email,
            "subject": user_subject,
            "message": user_message,
        }

        send_email(user_name, user_email, user_subject, user_message)
        
        return render_template("get_info.html", html_user_info=user_info)
    return render_template("index.html", html_form=form_python)

@app.route('/info')
def info_project():
    return render_template("info_project.html")

# @app.route('/contact', methods=["GET", "POST"])
# def user_contact():
#     form_python = ContactForm()

#     if form_python.validate_on_submit():
#         user_name = form_python.name.data
#         user_email = form_python.email.data
#         user_subject = form_python.subject.data
#         user_message = form_python.message.data

#         user_info = {
#             "name": user_name,
#             "email": user_email,
#             "subject": user_subject,
#             "message": user_message,
#         }

#         send_email(user_name, user_email, user_subject, user_message)
        
#         return render_template("get_info.html", html_user_info=user_info)
#     return render_template("contact_page.html", html_form=form_python)

def send_email(name, email, subject, message):
    #Create email
    user_info = f"""
    Here are information from user: \n
    Name: {name}, \n
    Email: {email}, \n
    Message: {message}.
    """
    msg = EmailMessage()
    msg.set_content(user_info)
    msg["Subject"] = f"{subject}"
    msg["From"] = my_email
    msg["To"] = my_email

    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=api_key_gmail)
        connection.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")