#Creating a simple calculator

#Display options to users
print("1 Addition")
print("2 Subtaction")
print("3 Multiplication")
print("4 Division")

#Users enters choice
choice=input("enter choice: ")

#Enter 2 numbers in which the operation will be performed
num1=float(input("enter number 1: "))
num2=float(input("enter number 2: "))

if choice == "1":
 print(num1, "+", num2, "=", (num1 + num2))
 
elif choice == "2":
 print(num1, "-", num2, "=", (num1 - num2))
 
elif choice == "3":
 print(num1, "*", num2, "=", (num1 * num2))
 
elif choice == "4":
 print(num1, "/", num2, "=", (num1 / num2))
 
else:
 print("invalid choice")
  
