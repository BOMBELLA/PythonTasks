#this program should make the user input a password  and check the length of the password if the password is weak it shows that the password very weak, also if the password is very weak or strong or even very strong.and the password shoould noy be less than 8 and above 16. 







password = input("Enter a number:")
passwordlength = len(password)

if passwordlength < 8:
       print("very weak")


if passwordlength < 8 & 16:
        print("strong")

                     
      

if passwordlength > 16:
       print("very strong")

