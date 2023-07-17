# ------------------------------Imports
from flask import Blueprint, render_template, redirect, url_for, request, send_from_directory
from myresume.single_page.forms import ContactForm
import smtplib
from email.message import EmailMessage
from config import ProductionConfig
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv


# ---------------------------Create Blueprint
single_page_blueprint = Blueprint('single-page', __name__, template_folder='templates/single_page')

# ---------------------------Get user info to send email
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# MY_EMAIL = os.getenv("my_email")
# API_KEY_GMAIL = os.getenv("api_key_gmail")
config_info = ProductionConfig()
MY_EMAIL_AWS = config_info.MY_EMAIL
API_KEY_GMAIL_AWS = config_info.API_KEY_GMAIL

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
    msg["From"] = MY_EMAIL_AWS
    msg["To"] = MY_EMAIL_AWS

    #Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL_AWS, password=API_KEY_GMAIL_AWS)
        connection.send_message(msg)

    #Return to home page
    return redirect(url_for("single-page.home"))


@single_page_blueprint.route('/info')
def info_project():
    return render_template("info_project.html")


@single_page_blueprint.route('/resume-download')
def download_resume():
    return send_from_directory(directory="static", path="assets/pdf/Paulina_Kimak_Resume.pdf", as_attachment=True)
