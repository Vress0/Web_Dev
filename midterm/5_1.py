import json

# 原始資料
person = [
    {"name": "Bob", "age": "20", "ID": 1, "languages": ["Python", "HTML"]},
    {"name": "Jack", "age": "21", "ID": 2, "languages": ["HTML", "CSS"]}
]

# 寫入 person.json（縮排2）
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2, ensure_ascii=False)

print("✅ person.json 已建立完成！")
