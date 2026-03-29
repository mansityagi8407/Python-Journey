# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is:")

# # if something wrong in the program then by this exception handling we detect the error and after the error code will be run. bcz program wil not hold after error 
# try:
#   for i in range(1,11):
#     print(f"{int(a)} * {i} = {int(a)*i}")
# except Exception as e:
#   print("Sorry some error occured")


# print("Some imp lines of code")
# print("End of program")


try:
   num = int(input("Enter an integer: "))
   a = [1,6,5,45]
   print(a[num])
except ValueError:
   print("Number entered is not an integer.")

except IndexError:
   print("Index error")