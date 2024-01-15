#PROJECT 1: NAME BAND GENERATOR
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")
#2. Ask the user for the city that they grew up in.
city = input("What is the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name= input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("The name of your band is " + city + " " + pet_name)

#PROJECT 2: TIP CALCULATOR
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? ") )
people = int(input("How many people to split the bill? "))
split = (total_bill*(1+(tip_percentage/100)))/people
# {:.2f} --> ROUND IT TO 2 DECIMAL PLACES 
split_bill = "{:.2f}".format(split)
print(f"Each person should pay : ${split_bill}")

#PROJECT 3: TREASURE ISLAND GAME
print('''
  *******************************************************************************
               |                   |                  |                     |
      _________|________________.=""_;=.______________|_____________________|_______
     |                   |  ,-"_,=""     `"=.|                  |
     |___________________|__"=._o`"-._        `"=.______________|___________________
               |                `"=._o`"=._      _`"=._                     |
      _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
     |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
     |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
               |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
      _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
     |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
     |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
     ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
     /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
     ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
     /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
     ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
     /______/______/______/______/______/______/______/______/______/______/[TomekK]
     ******************************************************************************* 
     ''')

print("Welcome to Treasure Island!")
name=input("What is your name?")
print(f"Hello {name}, your mission is to find the hidden treasure.")
print("I am going to ask you several questions that will help you find the treasure.\nGood luck and let's begin!")
q1=input("Imagine you are on a crossroad. Where do you go left or right?")
lower_q1=q1.lower()
if lower_q1 == 'left':
  print("Congratulations! You have reached the next level")
  q2 = input("Now, you have reach a lakeshore. Do you want to swim or try to find a boat? Please type swim or boat:")
  lower_q2=q2.lower()
  if lower_q2 =='boat':
    print("Congratulations! You have reached the next level")
    q3 = input("To get a boat, you need to choose between 3 different doors. Which one will you choose? Blue, Red or Yellow?")
    lower_q3 = q3.lower()
    if lower_q3 == 'blue':
      print("Game Over, eaten by beasts")
    elif lower_q3 == 'red':
      print("Game over, burned by fire")
    elif lower_q3 == 'yellow':
      print("Congratulations! You have found the boat and reached the next level")
    else:
      print("You chose a door that does not exist. Game Over")
      q4 = input("You have reached the final level. Where is the treasure? In the cave or in the forest? Please type cave or forest:")
      lower_q4 = q4.lower()
      if lower_q4 == 'cave':
        print("Congratulation, you win!! The treasure is in the cave")
      else:
        print("Game over, try again next time")
  else:
    print("Game Over, try again")
else:
  print("Game Over, try again")


        




