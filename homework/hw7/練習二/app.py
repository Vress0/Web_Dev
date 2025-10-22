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

@app.route("/students", methods=["POST"])
def add_student():
    body = request.get_json(silent=True) or {}
    data = load_data()
    required = ["id", "name", "email", "dept", "phone", "suggestion"]
    missing = [r for r in required if not str(body.get(r, "")).strip()]
    if missing:
        return jsonify({"錯誤": f"缺少欄位：{', '.join(missing)}"}), 400
    if any(s["id"] == body["id"] for s in data):
        return jsonify({"錯誤": f"學號 {body['id']} 已存在"}), 400
    data.append(body)
    save_data(data)
    return jsonify(body), 201

# 💡 如果 students.json 不存在就先建立空的
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)



if __name__ == "__main__":
    app.run(debug=True)
