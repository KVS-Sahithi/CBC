'''all the stuff that a user can navigate such 
 as home page navigation pages goes into this 
 part , all the authentication part such as 
 the login sign up page etc do not come under this part'''

from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route("/")
def home():
    return render_template("home.html")
