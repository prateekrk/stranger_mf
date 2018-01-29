import random
count=0
while(count<=100):
    j=input("press enter to roll a dice")
    r=random.randint(1,6)
    count=count+r
    print("your position",count)
    ladderList=[8,13,40,52,76]
    sanke_biteList=[11,25,38,65,89,93]
#ladder list
    if(count==ladderList[0]):
        count=37
    if(count==ladderList[1]):
        count=34
    if(count==ladderList[2]):
        count=68
    if(count==ladderList[3]):
        count=81
    if(count==ladderList[4]):
        count=76

#sanke bites
    if(count==sanke_biteList[0]):
        count=2
    if(count==sanke_biteList[1]):
        count=4
    if(count==sanke_biteList[2]):
        count=9
    if(count==sanke_biteList[3]):
        count=46
    if(count==sanke_biteList[4]):
        count=70
    if(count==sanke_biteList[5]):
        count=64

    if(count==100):
        print("you won")
    if(count<=100):
        count
        

    
