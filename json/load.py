# 需要import json
import json

with open('dump.json', 'r', encoding='utf-8') as file_object:
    numbers = json.load(file_object)
print(numbers)   #[1, 3, 5, 7, 9, 11, 13]
