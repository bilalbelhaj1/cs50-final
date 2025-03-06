from flask import Flask, render_template, redirect, request, flash, session
import helpers
import requests
app = Flask(__name__)
app.config["SECRET_KEY"] = "dgggggggggggggggyvcvcyvvcydycyvc"

def get_info(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'UuhnlMifttyuLLoDczpWFw==IWdhWcKpztzEZ6yR'})
    if response.status_code == requests.codes.ok:
       return response.json()
    else:
        return None

@app.route("/")
def index():
    return render_template("index.html")

# handle the user search
@app.route("/search")
def search():
    animal = request.args.get("animal")
    # handle the case when the user don't enter a anima name                                                   
    if not animal:

        flash("please type the animal name")
        return redirect('/')
    # check if the the entred by user is a valid animal
    result = get_info(animal)
    if len(result) == 0:
        flash("please enter a valid animal name", "warning")
        return redirect('/')
    
    # get the informations and images about the provided animal
    animal_data = helpers.get_animal_information(animal)
    if not animal_data:
        flash(f"sorry couldn't find any information about {animal}", "info")
        return redirect('/')
    
    # handle get request
    return render_template("search.html", animal_data=animal_data)



# register 
@app.route("/register", methods=["POST", "GET"])
def register():

    # handle the post request
    if request.method == "POST":
        
        # get the provided data
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        # validate if the user provided a username
        if not username:
            flash("Please enter a username", "danger")
            return redirect("/register")
        
        # validate if the user provided a password
        elif not password:
            flash("please provide a password", "danger")
            return redirect("/register")
        
        # validate if the user provided an email
        elif not email:
            flash("please enter your email")
            return redirect("/register")
        
        # check if the username already exists
        elif helpers.check_user(username):
            flash("username already exists", "warning")
            return redirect("/register")
        
        # check if the email already exists
        elif helpers.check_email(email):
            flash("email already exists", "warning")
        else:

            # register the user
            if helpers.add_user(username, email, password):
                flash("you are registered")
                return redirect("/")
            else:
                flash("somthing went wrong","danger")
                return redirect("/register")
    
    # handle get method
    return render_template("register.html")


# login
@app.route("/login", methods=["POST", "GET"])
def login():

    # handle the post method
    if request.method == "POST":

        # get the submited data
        username = request.form.get("username")
        password = request.form.get("password")

        # check if the user provided a username
        if not username:
            flash("please provide a username", "danger")
            return redirect("/login")
        
        # check if the user provided a password
        elif not password:
            flash("please provie a password", "danger")
        else:

            # validate the informations
            result = helpers.check_user_info(username, password)

            # check if the user exists
            if result == "user_not":
                flash("Invalid Username", "danger")
                return redirect("/login")
            
            # check if the password not correct
            elif result == "not_pass":
                flash("invalid password", "danger")
                return redirect("/login")
            
            # login the user
            else:
                flash(f"Welcome back,{result[1]}", "success")
                session["user_id"] = result[0]
                return redirect("/")
    # handle the get method 
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
