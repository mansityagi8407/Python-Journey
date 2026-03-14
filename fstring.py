# -------------------- STRING FORMATTING---------------- 
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Annu"
#print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")

price = 49.666666
txt = f"For only {price:.2f} dollars!"    # HERE 2F is used for showing the digit after POINT
print(txt)