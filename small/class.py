class Dog():
    def __init__(self, name, age):
        self.name = str(name).title()
        self.age = int(age)

    def run(self):
        print("Hey!master! I am"+self.name+" I can run!")

    def sleep(self):
        print("Oh master,I am tired,I am "+str(self.age)+" years old")


dog = Dog("lxx", 21)
dog.run()
while True:
    message = input("Do you want to sleep?(yes/no):")
    if message == 'yes':
        dog.sleep()
        break
    else:
        dog.run()

print(dog)
print(dog.name)
# print(dog.self) """么有这个属性""""