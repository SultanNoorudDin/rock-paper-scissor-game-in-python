import random

def play():
    user = input("what's your choice? (use initials to represent) \n rock / paper / scissor \n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return ('game tie')
    
    if isWon (user,computer):
        return ('you won')
    
    return 'you lost'
    

def isWon (player , computer):
    if (player == 'r'  and computer == 's') or ( player == 's' and computer == 'p') or ( player == 'p' and computer == 's'):
        return True


print(play())


# or like this:

# def play():
#     user = input("what's your choice? (use initials to represent) \n rock / paper / scissor \n")
#     computer = random.choice(['r','p','s'])

#     if user == computer:
#         print ('game tie')
    
#     if isWon (user,computer):
#         return ('you won')
    
#     if isWon(computer, user):
#         print ('you lost')
    

# def isWon (player , computer):
#     if (player == 'r'  and computer == 's') or ( player == 's' and computer == 'p') or ( player == 'p' and computer == 's'):
#         return True


# play()