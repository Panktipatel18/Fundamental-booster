print("WELCOME TO THE INTERACTIVE PERSONAL DATA COLLECTOR ")

name = input("Enter Your Name: ")

age = int(input("Enter Your Age: "))

height =float(input("Enter Your Height (in cm): "))

fav_number = int(input("Enter Your Favourite Number: "))

current_year = 2026
birth_year = current_year - age


age_after_10 =  age+ 10



print(f"NAME")
print("Value :",name)
print("Type :",type(name))
print("ID :",id(name))
print()
 

print(f"Age")
print("Value :",age)
print("Type :", type(age))
print("ID :", id(age))
print()


print(f"Height")
print("Value :", height)
print("Type :", type(height))
print("ID :" ,id(height))
print()

print(f"Favourite Number")
print("Value :", fav_number)
print("Type :", type(fav_number))
print("ID :", id(fav_number))
print()

print("/n")

print("Approximate Birth Year :",birth_year)

print("/n")
print("Thank you for using the Personal Data Collector")
print("Have A Great Day!")












