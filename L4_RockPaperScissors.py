import random
pp = 0
cp = 0
choice = ["rock", "paper", "scissors"]
print("Rock crushes scissors. Scissors cut paper. Paper covers rock")
while cp <= 2 and pp <= 2:
    cc = random.choice(choice)
    pc = input("Enter a choice (rock, paper, scissors): ").lower()
    print("You play " + pc + ", and the computer plays " + cc +".")
    if (pc == "rock" and cc == "paper") or (pc == "paper" and cc == "scissors") or (pc == "scissors" and cc == "rock"):
        cp += 1
        print("Computer wins!")
    elif (cc == "rock" and pc == "paper") or (cc == "paper" and pc == "scissors") or (cc == "scissors" and pc == "rock"):
        pp += 1
        print("You win!")
    elif cc == pc:
        print("It's a tie!")
    else:
        print("I think there is an error...")
    
    
if pp == 3:
    print("You are the final winner!")
elif cp == 3:
    print("Computer is the final winner!")


