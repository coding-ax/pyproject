# coding=utf-8
filename = 'progaamming.txt'
# w 写入模式 r读取模式（默认) a(附加模式) r+ 可读可写

strname = "熟悉的那一条街"
# with open(filename, 'w',encoding="utf=8") as file_object:
#     file_object.write(strname)
#     file_object.write('\n' + strname)

with open(filename, 'a', encoding='utf-8') as file_object:
    for item in range(0,100):
        file_object.write(strname);
    