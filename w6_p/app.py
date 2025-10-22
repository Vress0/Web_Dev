from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 從表單接收資料
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        dept = request.form.get("dept", "")
        phone = request.form.get("phone", "")
        suggestion = request.form.get("suggestion", "")

        # 把資料傳給 result.html
        return render_template("result.html",
                               name=name,
                               email=email,
                               dept=dept,
                               phone=phone,
                               suggestion=suggestion)
    # 第一次進入頁面（GET）
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
