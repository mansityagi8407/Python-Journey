# def Gmean (a,b):
#     mean = (a * b) / (a + b)
#     print(mean)

# def Greater(a,b):
#     if(a>b):
#         print("First number is greater than second")
#     else:
#         print("Second number is greater or equal")

# a = 9
# b = 8
# Greater(a,b)
# Gmean(a,b)

# c = 11
# d = 50
# Greater(c,d)
# Gmean(c,d)

# Greater(41,8)

# ---------FUNCTION (DEFAULT) ARGUMENTS--------

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is: ", sum / len(numbers))

average(5,6)
