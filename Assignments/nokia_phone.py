print("""

========================
=                      =
=    NOKIA 3310        =
=                      =
========================

1 -> Phonebook
2 -> Messages
3 -> Chat
4 -> Call register
5 -> Tones
6 -> Settings
7 -> Call Divert
8 -> Games
9 -> Calculator
10-> Reminders
11-> Clock
12-> Profiles
13-> Sim services 

""")
user_input = input("Enter a number: ")


if user_input == "1":

       print("""
Phonebook

1 -> Search
2 -> Service Number 
3 -> Add name
4 -> Erase
5 -> Edit
6 -> Assign Tone
7 -> Send b'card
8 -> Options
9 -> Speed Dials
10-> Voice Tags

""")

phonebook_input = input("Enter a number: ")

if phonebook_input == "1":
       print("Search")

elif phonebook_input == "2":
       print("Service Number")

elif phonebook_input == "3":
       print("Add name")

elif phonebook_input == "4":
       print("Erase")

elif phonebook_input == "5":
       print("Edit")

elif phonebook_input == "6":
       print("Assign Tone")

elif phonebook_input == "7":
       print("Send b' card")

elif phonebook_input == "8":
       print("""
Options
1-> Types of view
2-> Memory Status
""")

options_input = input("Enter a number: ")

if options_input == "1":
       print("Types of View")

elif options_input == "2":
       print("Memory Status")
else:
       print("Invalid number")

if phonebook_input == "9":
       print("Speed Dials")

elif phonebook_input == "10":
       print("Voice Tags")
else:
       print("Invalid number")









                                                 
