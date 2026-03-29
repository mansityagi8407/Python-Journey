def func1():
    try:
        a = [1,6,8,4]
        i = int(input("Enter the index: "))
        print(a[i])
        return 1
    except:
        print("Some error occured")
        return 0
    
    finally:
        print("Iam always executed")

x = func1()
print(x)