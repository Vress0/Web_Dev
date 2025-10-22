import json

with open('person.json', 'r') as f:
    person_data = json.load(f)

my_data = {
    "name": "Ting",  
    "age": "19",   
    "sex": "F",         
    "ID": 3,            
    "languages": ["None", "None"]  
}

person_data.append(my_data)

with open('partner.json', 'w') as f:
    json.dump(person_data, f, indent=4)

print("已成功將資料寫入 partner.json")
