import random
import string
c=['rock','scissor','paper']
p1=random.choice(c)
p2=random.choice(c)
r="rock"
p="paper"
s="scissor"

print(p1,"=player 1")
print(p2,"=player 2")
if(p1==p2):
    print("Game tie")
elif p1=='rock':
    if p2=='scissor':
        print("p1 won")
    else:
        print('p2 won')
elif p1=='rock':
    if p2=='paper':
        print("p2 won")
    else:
        print('p1 won')
elif p1=='scissor':
    if p2=='paper':
        print('p2 won')
    else:
        print('p1 won')
