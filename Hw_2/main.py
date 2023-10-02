from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "167e4a8b67baa8ff138a741997adbc2273bd1c76535752e2708be20c2eed1f55"


@app.route("/", methods=["GET", "POST"])
def login():
    context = {"login": "Авторизация"}
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        return redirect(url_for("success"))
    return render_template("login.html", **context)


@app.route("/success/", methods=["GET", "POST"])
def success():
    if "name" in session:
        context = {
            "name": session["name"],
            "email": session["email"],
            "title": "Добро пожаловать",
        }
        if request.method == "POST":
            session.pop("name", None)
            session.pop("email", None)
            return redirect(url_for("login"))
        return render_template("success.html", **context)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)