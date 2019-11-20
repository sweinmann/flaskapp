from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def index(title="Five9 Generic App", author="Five9 Generator"):
    return render_template("index.html", title="The New Five9 App", author="Scott Weinmann")

if __name__ == "__main__":
    app.run()
