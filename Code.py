import random

print("LETS PLAY GUESS THE NUMBER GAME".center(50,"*"))

print("your guessing limit:")

dict1={1:'1 to 10',2:'1 to 100',3:'1 to 1000'}

for key,value in dict1.items():
    print(key,"-->",value)

print("YOU HAVE TO GUESS THE NUMBER IN 5 COUNTS ONLY:".center(50,"*"))
try:
    choose=int(input('Enter your guess limit:'))

    if len(dict1.keys())>=choose:
        a,b=int(dict1[choose][0]),int(dict1[choose][5:])
        Randnumber=random.randint(a,b)
        success=0
        count=0
        while success==0 and count<=5:
            guess=int(input("PLEASE GUESS THE NUMBER IN YOUR CHOSEN LIMIT:"))
            count+=1
            if guess>=a and guess<=b:
                if guess==Randnumber:
                    print("CONGRAULATIONS,YOU GUESS THE RIGHT NUMBER IN:",count,"COUNTS")
                    success=1
                elif guess>Randnumber:
                    print("HINT: YOU GUESS TOO HIGH NUMBER")
                else:
                    print("HINT:YOU GUESS TOO LOW NUMBER")
            else:
                print("PLEASE GUESS NUMBER IN BETWEEN YOUR LIMIT INCLUSIVELY:")
        if success==1:
            print("WELL PLAYED,WANNA PLAY AGAIN")
    else:
        print('PLEASE TRY AGAIN LATER.')
except:
    print('PLEASE TRY AGAIN LATER. and ENTER VALID VALUE')
    

