# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip());

# with open('pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

# for line in lines:
    # print(line.rstrip())

#rstrip 右边空格 lstrip 左边空格 strip 左右空格 
 
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

print(float(pi_string) + 5)

num = str(input("please type the num:"))
if num in pi_string:
    print("yes!")
else:
    print("no!");