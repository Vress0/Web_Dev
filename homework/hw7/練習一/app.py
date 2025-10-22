from flask import Flask, render_template, request
import json, os

app = Flask(__name__)
JSON_FILE = "students.json"

def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_student = {
            "id": request.form.get("id", ""),
            "name": request.form.get("name", ""),
            "email": request.form.get("email", ""),
            "dept": request.form.get("dept", ""),
            "phone": request.form.get("phone", ""),
            "suggestion": request.form.get("suggestion", "")
        }
        data = load_data()
        data.append(new_student)
        save_data(data)
        return render_template("result.html", student=new_student)
    return render_template("reg.html")



# 💡 如果 students.json 不存在就先建立空的
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
