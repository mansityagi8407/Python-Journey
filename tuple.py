"""TUPLE can't changable like LIST"""
# t = (1,5,8,6)
# print(t)
# print(len(t))
# print(t[0:3])

""" TUPLE OPERATIONS"""
# t = t + ( 2,9)
# print (t) 


# """ TUPLE REPETITION"""
# t = ("Hello",)
# print(t * 3)



# index = (1,5,9,6,3)
# temp= list(index)
# temp.append(2)
# temp.pop(1)
# temp[2]=8
# index = tuple(temp)
# print(index)

tuple1 = (0, 1, 2, 5, 5, 7, 3, 8,3)
res = tuple1.count(3)
# res = tuple1.index(3)
print("count of 3 in tuple1 is:", res)

