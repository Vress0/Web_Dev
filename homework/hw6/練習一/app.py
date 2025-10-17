from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/result", methods=["POST"])
def result():
    # 接收使用者輸入的資料
    name = request.form.get("name")
    student_id = request.form.get("student_id")
    phone = request.form.get("phone")

    return render_template("result.html", name=name, student_id=student_id, phone=phone)

if __name__ == "__main__":
    app.run(debug=True)
