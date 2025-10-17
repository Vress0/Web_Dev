from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        id = request.form.get("id")
        email = request.form.get("email")
        dept = request.form.get("dept")
        phone = request.form.get("phone")
        suggestion = request.form.get("suggestion")

        return redirect(url_for(
            "result",
            name=name,
            id=id,
            email=email,
            dept=dept,
            phone=phone,
            suggestion=suggestion
        ))
    return render_template("register.html")

@app.route("/result")
def result():
    name = request.args.get("name")
    id = request.args.get("id")
    email = request.args.get("email")
    dept = request.args.get("dept")
    phone = request.args.get("phone")
    suggestion = request.args.get("suggestion")
    return render_template(
        "result.html",
        name=name,
        id=id,
        email=email,
        dept=dept,
        phone=phone,
        suggestion=suggestion
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port='9000',debug=True)
