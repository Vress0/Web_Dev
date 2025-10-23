import json

# 讀取 person.json
with open('person.json', 'r', encoding='utf-8') as f:
    person_data = json.load(f)

print("✅ person.json 內容如下：")
print(person_data)
