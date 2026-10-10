import random
#problem 1
name=input("Whats your name? ")
fav_color=input("Whats your favorite color? ")
age=int(input("How old are you? "))
print(f"Hello {name}\n, Your fav color is {fav_color}\n and in 10 years you will be {age+10}!")


#problem 2
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
operator=input("Enter your operator: ")
num1float=float(num1)
num2float=float(num2)
if operator == "+":
    print(num1float+num2float)
elif operator == "-":
    print(num1float-num2float)
elif operator == "*":
    print(num1float*num2float)
else:
    print(num1float/num2float)

#problem3
n=int(input("Your Number: "))
for n in range(1,n+1):
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

#problem4
mnum=int(input("Enter ur number: "))
for i in range(1,11):
    print(f"{mnum} x {i} = {mnum*i}")

#problem5
n=int(input("Starting num: "))
while n>0:
    print(n)
    n-=1
    print("Liftoff!")

#problem6
while True:
    try: 
        userage=int(input("How old are you? "))
        break
    except ValueError:
        print("Not a whole number stupid, try again >(") 

 

#problem8
choices = ["rock", "paper", "scissors"]
while True:
    user=input("Rock, Paper, Scissors? ")
    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer=random.choice(choices)
    print(f"computer chose: {computer}")

    if user == computer:
        print("tie!")
    elif user == "rock" and computer == "paper":
        print("computer wins")
    elif user == "paper" and computer == "rock":
        print("you win")
    elif user =="scissors" and computer == "rock":
        print("you win")
    elif user == "rock" and computer == "scissors":
        print("computer wins")

