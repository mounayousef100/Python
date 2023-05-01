from math import *;
x = 'mouna yousef qa'

print(x.index('qa'))
print(len(x))
print(x.replace("q", "p"))
print(floor(7.7))
print(ceil(7.4))
print(abs(-7))
name = input("enter yuor name")
print("you won "+ name)
num1 = input("enter number : ")
num2 = input("enter number : ")
result = float(num1)+ float(num2)
print(result)
w = [1,2,7,4,5]
e = ["mouna","ahmad","kaled"]
w.extend(e)
w.insert(1, "amal")
w.append("ahmad")
w.sort(reverse=True)
e.sort()
e.remove("ahmad")
e.clear()
print(w)
print(e)
tuples = (1,2,4,5)
