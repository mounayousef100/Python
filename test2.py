
info = {
    "name": "ahmad",
    "age": 25,
    "country":"jordan"
}
print(info["name"])
print(info.get("age"))
print(info.get("id","not found"))


def firstfunction(name):
    print("my name is : "+ name)
    firstfunction("amal")
