try:
    num = int(input('enter number :'))
    print(num)
    x = 1/0
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)
print('test')