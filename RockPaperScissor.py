import random
user_choice=int(input("Enter your choice:type 0 for Rock, 1 for paper, 2 for scisoors"))
computer_choice=random.randint(0,2)
print("Computer choice:")
print(computer_choice)
if(user_choice == computer_choice):
    print("its draw.")
elif(user_choice == 0 and computer_choice == 2):
    print("You win.")
elif(computer_choice == 0 and user_choice == 2):
    print("You lose.")
elif(user_choice > computer_choice):
    print("You win.")
elif(computer_choice > user_choice):
    print("You lose")