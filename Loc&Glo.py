# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local x is {x}")
#     print("Hello Mansi")
# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")



x = 6
print(x)

def hello():
    global x
    x = 3
hello()
print(x)