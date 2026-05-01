""" READING A FILE"""

# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


""" WRITING A FILE"""

# f= open('myfile.txt', 'w')
# f.write('Miss Awesome')

""" multile times run the program file also append tht much time."""

# f= open('myfile.txt', 'a')
# f.write('Miss Awesome')
# f.close()


""" Automatically close  file by WITH"""

with open('myfile.txt','a') as f:
    f.write("Hey I am inside with")



