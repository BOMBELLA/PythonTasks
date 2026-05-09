#write an application
#using a for loop
#input three scores using the letter grading
#sum up the three scores
#divide by three
# return the letter grading


for score in range(2):
       score_one = input("Enter score one = ")

       score_two = input("Enter score two = ")

       score_three = input("Enter score three = ")

       sum = score_one + score_two + score_three
       result = sum / 3
       
       if(result > 90 and result <= 100):

              print("A")

       if(result > 70 and result <= 80):

              print("B")

       if(result > 0 and result <= 60):

              print("C")


print(result)      
       
       
        


