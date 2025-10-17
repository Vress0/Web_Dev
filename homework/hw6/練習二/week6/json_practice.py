import json

# 1️⃣ 讀取原始 personc.json 檔案
with open("personc.json", "r", encoding="utf-8") as f:
    original_data = json.load(f)

# 2️⃣ 建立兩位新同學的資料
my_data = {
    "姓名": "品沅",
    "性別": "男",
    "學號": "B1123456",
    "專長": ["網頁開發", "資料分析"]
}

xiaobao_data = {
    "姓名": "小寶",
    "性別": "女",
    "學號": "B1098765",
    "專長": ["平面設計", "影片剪輯"]
}

# 3️⃣ 把三筆資料放進同一個 list
all_students = [original_data, my_data, xiaobao_data]

# 4️⃣ 寫入新的 JSON 檔案 personc_final.json
with open("personc_final.json", "w", encoding="utf-8") as f:
    json.dump(all_students, f, ensure_ascii=False, indent=2)

print("✅ 已成功建立 personc_final.json")

# 5️⃣ 讀取剛剛建立的檔案並顯示三位同學資料
with open("personc_final.json", "r", encoding="utf-8") as f:
    final_data = json.load(f)

print("\n📋 三位同學資料：\n")
for s in final_data:
    print(f"姓名：{s['姓名']}")
    print(f"性別：{s['性別']}")
    print(f"學號：{s['學號']}")
    print(f"專長：{', '.join(s['專長'])}")
    print("─" * 30)
