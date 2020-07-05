import yaml


class Animal:
    name:str = "default"
    color:str = "default"
    age: int = 0
    gender: str = "default"


    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def run(self):
        print(f"{self.name} is running.")

    def shout(self):
        print(f"{self.name} is shoutting.")


class Cat(Animal):
    hair:str = "short hair"

    def __init__(self,name,color,age,gender):
        super(Cat,self).__init__(name,color,age,gender)

    def catch_mourse(self):
        print(f"{self.name} catchs a mourse.")

    def shout(self):
        print(f"{self.name} is MiaoMiao shoutting.")

class Dog(Animal):
    hair:str = "long hair"

    def __init__(self,name,color,age,gender):
        super(Dog,self).__init__(name,color,age,gender)

    def housekeep(self):
        print(f"{self.name} can housekeeping.")

    def shout(self):
        print(f"{self.name} is WangWang shoutting.")


if __name__ == '__main__':
    with open("Animal.yml") as f:
        datas = yaml.safe_load(f)

    print(datas)
    cat_data = datas["mycat"]
    mycat = Cat(cat_data["name"],cat_data["color"], cat_data["age"], cat_data["gender"])
    mycat.catch_mourse()
    print(
        f"The cat's name is {mycat.name},is {mycat.color}, {mycat.age} years old, has {mycat.hair} and catch a mouse.")

    dog_data = datas["mydog"]
    mydog = Dog(dog_data["name"], dog_data["color"], dog_data["age"], dog_data["gender"])
    mydog.housekeep()
    print(f"The dog's name is {mydog.name},is {mydog.color}, {mydog.age} years old, has {mydog.hair}.")






