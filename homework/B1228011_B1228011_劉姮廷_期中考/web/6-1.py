import json
person = [
    {"name": "Bob", "age": "20", "sex": "M", "ID": 1, "languages": ["python", "HTML"]},
    {"name": "Jack", "age": "21", "sex": "M", "ID": 2, "languages": ["HTML", "CSS"]}
]

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

print("已成功將資料寫入 person.json")
