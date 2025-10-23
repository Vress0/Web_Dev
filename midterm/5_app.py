from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# 路由：接收 POST 請求
@app.route('/add_person', methods=['POST'])
def add_person():
    # Step 1：讀取原本的 person.json
    if os.path.exists('person.json'):
        with open('person.json', 'r', encoding='utf-8') as f:
            persons = json.load(f)
    else:
        persons = []

    # Step 2：取得 Postman 傳來的資料
    new_person = request.get_json()

    # Step 3：把新資料加入列表
    persons.append(new_person)

    # Step 4：寫入新的 partner.json
    with open('partner.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    # Step 5：回傳成功訊息
    return jsonify({
        "message": "✅ 已成功新增資料並寫入 partner.json！",
        "total_records": len(persons)
    }), 200
@app.route('/')
def home():
    return "✅ Flask 伺服器正在運作中！請使用 POST /add_person 新增資料。"


if __name__ == '__main__':
    app.run(debug=True)
