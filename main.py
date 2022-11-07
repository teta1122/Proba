

# new comment added
# megegy
import json5

with open("json.json5", "r") as file:
    data = json5.load(file)
    print(data)



def my_function(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs["KEY"])
    print(kwargs["KEY2"])


#my_function("alma", 1, 4, "kutya", KEY="Tomi", KEY2= "Tomik2")

class Person():

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender

# getter
    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str) -> None:
        self.__name = value

p1 = Person("Tomi", 26, "male")
print(p1.Name)
p1.Name = "Tamas"
print(p1.Name)
