#collect an input asking users to input a password
#use len to check the length and strength
#use a control staement to compare
#if the password is greater than 6 and less than or equals 10 then the password is medium
#if the password is less than 6 then the password is weak
#if the password is greater than 10 then it is strong
#if the password is less than 1 then the password is invalid


password = input("Enter your password : ")

len(password)

if(password > 6 and <= 10):
       print("Medium")

elif(password > 6):
       print("Weak")

else if(password > 10):
       print("Strong")

else(password < 1):
       print("Invalid")

