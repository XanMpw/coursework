from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/account")
def about():
    return render_template("account.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/watchlists")
def watchlists():
    return render_template("watchlists.html")

if __name__ == "__main__":
    app.run(debug=True)