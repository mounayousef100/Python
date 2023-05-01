name = 'mouna'
age = 28
country = 'jordan'
print("my name is %s my age is %s my country is %s" %(name,age,country))
print("my nationality is %s" % country)
# %s %d %f 
print("my age is %d " % age)
print("my age is %s" % age)
print("my age is %.3f"% age)
print("my name is {}".format(name))
print("my name is {} my age is {}".format(name,55))
print("the price is {:,}".format(1000000))
print("the price is {:.4f}".format(1000000))
a = 1
b = 2
c = 3 
print("the number is {2:d} {0:f} {1:d}".format(a,b,c))
print(f"the number is {a:d} {b:f} {c:f}")