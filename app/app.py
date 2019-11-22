from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def index(title="Five9 Generic App", author="Five9 Generator"):
    return render_template("index.html", title="The New Five9 App", author="Scott Weinmann")

@app.route("/login", methods=['GET', 'POST'])
def login(title="Five9 Generic App Login"):
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Incorrect username or password. Access Denied."
        else:
            logged_in=True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()
