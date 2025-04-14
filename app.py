from flask import Flask, render_template, redirect, url_for, request, flash, session
from auth import signup_user, login_user
from donor import add_donor, get_donors, search_donors, delete_donor
from db import create_tables

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize database
create_tables()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if signup_user(username, password):
            flash("Signup successful! Please login.", "success")
            return redirect(url_for("login"))
        else:
            flash("Username already exists!", "danger")
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if login_user(username, password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials!", "danger")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    donors = get_donors()
    return render_template("dashboard.html", donors=donors)

@app.route("/add_donor", methods=["GET", "POST"])
def add_donor_route():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        blood_group = request.form["blood_group"]
        contact = request.form["contact"]
        if name and age and blood_group and contact:
            add_donor(name, age, blood_group, contact)
            flash("Donor added successfully!", "success")
        else:
            flash("All fields are required!", "danger")
        return redirect(url_for("dashboard"))
    return render_template("add_donor.html")

@app.route("/search_donor", methods=["GET", "POST"])
def search_donor_route():
    if "username" not in session:
        return redirect(url_for("login"))
    donors = []
    if request.method == "POST":
        blood_group = request.form["blood_group"]
        if blood_group:
            donors = search_donors(blood_group)
            if not donors:
                flash("No donors found for the specified blood group.", "info")
        else:
            flash("Please enter a blood group to search.", "danger")
    return render_template("search_donor.html", donors=donors)

@app.route("/delete_donor/<int:donor_id>")
def delete_donor_route(donor_id):
    if "username" not in session:
        return redirect(url_for("login"))
    delete_donor(donor_id)
    flash("Donor deleted successfully!", "success")
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
