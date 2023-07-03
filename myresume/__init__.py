from flask import Flask
import secrets



#------------------------Create app
application = Flask(__name__)
application.config["SECRET_KEY"]= secrets.token_hex(32)

#------------------------Register Blueprints
from myresume.single_page.views import single_page_blueprint

application.register_blueprint(single_page_blueprint, url_prefix='/')