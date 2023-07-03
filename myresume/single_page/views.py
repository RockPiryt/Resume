# ------------------------------Imports
from flask import Blueprint, render_template, redirect, url_for, request

from myresume.single_page.forms import ContactForm
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv


# ---------------------------Create Blueprint
single_page_blueprint = Blueprint('single-page', __name__, template_folder='templates/single_page')

# ---------------------------Get user info to send email
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
my_email = os.getenv("MY_EMAIL")
api_key_gmail = os.getenv("APP_PASSWORD_GMAIL")

# ---------------------------Create views


@single_page_blueprint.route("/", methods=["GET", "POST"])
def home():
    '''Main page'''

    # Crete Contact form
    contact_form = ContactForm()

    # Get data from user
    if contact_form.validate_on_submit():
        user_name = contact_form.name.data
        user_email = contact_form.email.data
        user_subject = contact_form.subject.data
        user_message = contact_form.message.data

        #Send data to send_email route
        return redirect(url_for("single-page.send_email",
                                form_name=user_name,
                                form_email=user_email,
                                form_subject=user_subject,
                                form_message=user_message
                                ))
    return render_template("index.html", html_form=contact_form)


@single_page_blueprint.route("/send-email", methods=["GET", "POST"])
def send_email():
    '''Send email with form data'''

    #Get data from form
    name = request.args.get("form_name")
    email = request.args.get("form_email")
    subject = request.args.get("form_subject")
    message = request.args.get("form_message")

    # Create email
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

    #Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=api_key_gmail)
        connection.send_message(msg)

    #Return to home page
    return redirect(url_for("single-page.home"))


@single_page_blueprint.route('/info')
def info_project():
    return render_template("info_project.html")
