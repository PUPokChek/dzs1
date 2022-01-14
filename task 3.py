choice = input("let's start game with your choice: ")
c = ['rock','paper','scissors']
if choice != c[0] and choice != c[1] and choice != c[2]:
    print ("Choice correct value")
else:    
    from random import randint
    r = randint(0,2)
    print("computer choice: " +c[r])
if choice==c[0] and r ==1:
    print("You lose")
if choice==c[1] and r ==0:
    print("You win")
if choice==c[0] and r ==2:
    print("You win")
if choice==c[1] and r ==2:
    print("You lose")
if choice==c[2] and r ==0:
    print("You lose")
if choice==c[2] and r ==1:
    print("You win")
if c[r] == choice:
    print("Draw")

    
    
