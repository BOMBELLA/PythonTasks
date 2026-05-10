#collet two inputs and an operator
#give them reference names
#do a simple calculation using plus,minus and product
# using control statements
#print out the results

first_digit = int(input("Enter first number :" ))
second_digit = int(input("Enter second number : "))
operator = input("Enter an operator : ")

if(operator == "+"):
       result = first_digit + second_digit
print(result)

elif(operator == "-"):
       result = first_digit - second_digit 
print(result)

elif(operator == "*"):
       result = first_digit - second_digit  
print(result)     
 
else(operator == "/"):
       result = first_digit / second_digit 
print(result)
