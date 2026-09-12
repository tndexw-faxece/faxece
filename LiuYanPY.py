from flask_cors import CORS

from flask import *
app = Flask(__name__)
CORS(app)

CORS(app, origins=["https://faxece.github.io/faxece"])

messages = []

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("BoardPage.html",messages=messages)

@app.route("/post",methods=["POST"])
def post():
    name = request.form.get("name")
    msg = request.form.get("message")
    messages.append({"name":name,"msg":msg})
    return redirect("/")
import os

if __name__ == "__main__":
    port = int(os.environ.get("POST", 5000))
    app.run(host="0.0.0.0",port=port,debug=False)
