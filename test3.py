
def firstfunction(name,age):
    print("my name is " + name +" my age is "+str(age))
firstfunction('amal',23)
def calc(num1,num2):
    print("aaaaaaa")
    return num1+num2
print(calc(10, 4))
    


def calchours(age):
    return "Your age in hours is: " + str(age * 365 * 24) + " hours"

print(calchours(int(input("Enter your age: "))))