#collect input of age
#using control statements
value = input("What is your age : ")
price = 0
age = 0
if(age < 5):
       print("Free")

elif(age >= 5 and age <= 13):

       print("$5")

elif(age >= 13 and age <= 64):
       
       print("$12")

elif(age == 65 and age <= 100):

       print("$8")
else:
       print("Invalid age")
