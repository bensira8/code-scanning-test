from flask import Flask, request
app = Flask(__name__)

class User(models.Model):
    pass

@app.route("/users/<username>")
def show_user():
    username = request.args.get("username")
