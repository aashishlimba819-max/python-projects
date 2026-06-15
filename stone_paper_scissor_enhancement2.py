import random
import getpass
print("Welcome to rock , paper and scissor game!")
choice=("r","s","p","y","n")
choice1=("r","p","s")
run=0
store_win=0
store_lose=0
store_tie=0
player1_win=0
player2_win=0
want_to_play=input("Do you want to play with computer or friend ?(c/f)").lower()
if(want_to_play=="c"):
    while True :   
        choose=input("Select one stone paper or scissor? (r/p/s):").lower() 
        if choose not in choice:
            print("Invalid choice")
        guess=random.choice(["Rock 🪨","Paper 📃","Scissor ✂️"])  
        if(choose=="r"):
            print("you choose Rock 🪨","\n","computer choose ",guess)
            if(guess=="Paper 📃"):
                print("You lose!")
                store_lose+=1
            elif(guess=="Scissor ✂️"):
                print("You Win!")
                store_win+=1
            elif(guess=="Rock 🪨"):
                print("match tie!")
                store_tie+=1
        if(choose=="p"):
            print("you choose Paper 📃","\n","computer choose ",guess)
            if(guess=="Scissor ✂️"):
                print("You lose!")
                store_lose+=1
            elif(guess=="Rock 🪨"):
                print("You Win!")
                store_win+=1
            elif(guess=="Paper 📃"):
                print("match tie!")
                store_tie+=1
        if(choose=="s"):
            print("you choose Scissor ✂️","\n","computer choose ",guess)
            if(guess=="Rock 🪨"):
                print("You lose!")
                store_lose+=1
            elif(guess=="Paper 📃"):
                print("You Win!")
                store_win+=1
            elif(guess=="Scissor ✂️"):
                print("match tie!")
                store_tie+=1  
        ask=input("want to play again ?(y/n)")
        if(ask=="n"):
            print("you Win :",store_win,", you Lose :",store_lose,", Match ties :",store_tie,sep="")
            break
        if(ask!="y" and ask!="n"):
            while ask!="y" and ask!="n":
                print("Invalid choice")
                ask=input("want to play again ?(y/n)")    
    if(store_win>store_lose):
        print("You overall win the game")
    elif(store_lose>store_win):
        print("You overall lose the game")
    elif(store_win==store_lose):
        print(" overall the game is tie")         
    print("Thanks for playing!")
if(want_to_play=="f"):
    while True:
        if(run==0):
            player1=input("enter player1 name:")
            player2=input("enter player2 name:")
        select1=getpass.getpass("player1 choose (r/p/s):").lower()
        select2=getpass.getpass("player2 choose (r/p/s):").lower()
        run+=1
        if (select1 not in choice1):
            print("Invalid choice")
            continue
        if (select2 not in choice1):
            print("Invalid choice")   
            continue
        if(select1=="r" and select2=="r"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print("match tie")
        elif(select1=="s" and select2=="s"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print("match tie")   
        elif(select1=="p" and select2=="p"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print("match tie")    
        elif(select1=="r" and select2=="p"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print(player2,"Win!")
            player2_win+=1
        elif(select1=="s" and select2=="r"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print(player2,"Win!")
            player2_win+=1
        elif(select1=="p" and select2=="s"):
            print(player1,"choose:",select1,player2,"choose:",select2)
            print(player2,"Win!") 
            player2_win+=1
        else:
            print(player1,"choose:",select1,player2,"choose:",select2)
            print(player1,"Win!")   
            player1_win+=1
        ask1=input("want to play again ?(y/n)")
    
        if(ask1=="n"):
            print(player1,"win:",player1_win,player2,"win:",player2_win)
            print("Thanks for playing!!")
            if(player2_win>player1_win):
                print(player2,"Win!")
            elif(player1_win>player2_win):
                print(player1,"win!!")
            else:
                print("match tie")
            break            
        if(ask1!="y" and ask1!="n"):
            while ask1!="y" and ask1!="n":
                print("Invalid choice")
                ask1=input("want to play again ?(y/n)")

elif(want_to_play!="c" and want_to_play!="f"):
    print("Inalid choice")             


