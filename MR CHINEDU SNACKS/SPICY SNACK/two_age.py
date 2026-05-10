#take two inputs
#the inputs should be from 1--80
#check and calculate  the fathers age when he is twice as old as his son 
#multiply fathers age by  
#the age should always be higher or equal to 0
#whether it is in the past or present or even even future .

current_father_age = int(input("Enter the current fathers age: "))

current_son_age = int(input("Enter the cuurent sons age: "))
result  = current_father_age - (2 * current_son_age)

if(result < 0):
       print("You just entered an invalid input...")

else:
       print(result)
#if(current_father_age >= current_son_age):
#       print("Father current age =")

     
