from flask import Flask, render_template, request

app = Flask(__name__)

# 首頁導向：直接顯示註冊表單
@app.route("/")
def index():
    return render_template("reg.html")

# 註冊頁：處理表單送出
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        dept = request.form.get("dept")
        phone = request.form.get("phone")
        suggestion = request.form.get("suggestion")
        return render_template(
            "result.html",
            name=name,
            email=email,
            dept=dept,
            phone=phone,
            suggestion=suggestion
        )
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(debug=True)
