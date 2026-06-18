import random
no_of_time_guess=0
number=random.randint(1,100)
#print(number)
guess_no=1
while (guess_no!=number):
    guess_no = int(input("Guess the number (between 1 to 100):"))
    no_of_time_guess+=1
    if(number-5<=guess_no<=number+5 and guess_no!=number):
        print("close the number!  Try again.")
    elif(guess_no>number+5):
        print("Too High! Try again.")   
    elif(guess_no<number-5):
        print("Too Low!  Try again.")   
    if(guess_no==number):
        print("Congratulation! you guessed the in",no_of_time_guess,"attempts")
        break
    # no_of_time_guess+=1
    # if(no_of_time_guess==10):
    #     print("sorry! your attempts is ended")
    #     break
# print("Congratulation! you guessed the in",no_of_time_guess,"attempts")    