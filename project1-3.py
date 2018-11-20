print("Rock...")
print("Paper...")
print("Scissors...")

import random
player=input("Player make your move: ").lower()
rand_num=random.randint(0,2)
if rand_num==0:
   computer="rock"
elif rand_num==1:
   computer="paper"
else:
   computer="scissors"
print(f"computer plays {computer}")
if player==computer:
    print("It is a tie!!!!!!!!")
elif player=="rock":
   if computer=="scissors":
      print("player wins!")
   elif computer=="paper":
      print("computer wins!")
   else:
      print("Something went wrong")
elif player=="paper":
   if computer=="scissors":
      print("computer wins!")
   elif computer=="rock":
      print("player wins!")
   else:
      print("Something went wrong")   
elif player=="scissors":
   if computer=="paper":
      print("player wins!")
   elif computer=="rock":
      print("computer wins!")
   else:
      print("Something went wrong")
else:
   print("Please enter a valid move!!!")
