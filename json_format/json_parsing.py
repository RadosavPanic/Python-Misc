import json


class User:
    static_data = "class data"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def to_json(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return self.name + " " + self.surname

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    @staticmethod
    def f(arg):
        print(User.static_data + arg)
        return


dictUser = User("John", "Doe").to_json()
print(dictUser)

fp = open("jsondata.txt", "w")
json.dump(dictUser, fp)
fp.close()

objUser = User.from_json(dictUser)
print(objUser)

fp = open("jsondata.txt", "r")
print(User.from_json(json.load(fp)))
fp.close()

User.f(" <--")

