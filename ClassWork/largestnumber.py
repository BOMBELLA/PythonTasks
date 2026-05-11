def largest_digit (digit_one, digit_two , digit_three):


       """return the largest of the three digit"""
       maximum =  digit_one        

       if digit_two  > maximum:
              maximum = digit_two
       if digit_three > maximum:
              maximum = digit_three
       return maximum
print(largest_digit(89,87,54))

                    
