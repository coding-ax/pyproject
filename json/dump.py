import json
numbers = [1, 3, 5, 7, 9, 11, 13]

filename = 'dump.json'
with open(filename, 'w', encoding='utf8') as file_object:
    #第一个参数是要存储的数据，第二个参数是可以用于存储数据的文件对象
    json.dump(numbers, file_object)
