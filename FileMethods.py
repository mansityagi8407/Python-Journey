f = open('docsfile.txt', 'r')
while True:
    line = f.readline()
    # print(line)
    if not line:
        print(line, type(line))
        break
    print(line)
