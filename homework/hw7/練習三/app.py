from flask import Flask, request, jsonify
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

@app.route("/students/<sid>", methods=["PATCH"])
def update_student(sid):
    data = load_data()
    student = next((s for s in data if s["id"] == sid), None)
    if not student:
        return jsonify({"錯誤": f"找不到學號 {sid} 的資料"}), 404

    body = request.get_json(silent=True) or {}
    for key in ["email", "phone", "suggestion"]:
        if key in body:
            student[key] = body[key]
    save_data(data)
    return jsonify(student), 200


# 💡 如果 students.json 不存在就先建立空的
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    app.run(debug=True)
