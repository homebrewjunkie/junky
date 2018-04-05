from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return "¯\_(ツ)_/¯"

@app.route("/ph")
def ph():
    return render_template("ph.html")
    
if __name__ == "__main__":
    app.run("debug=True, host="0.0.0.0", port=80)

