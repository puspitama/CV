from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(_name_)


@app.route("/")
def halamanCV():
    return render_template("index.html")

if _name_ == "_main_":
    run_with_ngrok(app)
    app.run()