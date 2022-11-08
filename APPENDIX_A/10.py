def add(a, b):
    return a+b

print(add(3, 4))
print((lambda a, b: a+b)(3, 4))
# (lambda 매개변수1, 매개변수2, ... : return값)(인수1, 인수2, ...)