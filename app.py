from flask import Flask , render_template , request , redirect , url_for ,flash

app = Flask(__name__)
app.secret_key = 'johN@123_my_unique_secret'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        flash("Message sent successfully!", "success")
        # Optionally save to a file/database or send an email
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
 
