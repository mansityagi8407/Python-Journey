dic = {
    25: "Chirag",
    34: "Aryan",
    47: "Mansi",
    56: "Vanshi"
}

print(dic)
print(dic[47])

# get is used for showing none either error when key is not exists
print(dic.get(45))
# key is used for show all the elements & value is for values
print(dic.keys())
print(dic.values())

print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")