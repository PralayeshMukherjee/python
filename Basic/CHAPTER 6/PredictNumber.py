import random;

number = random.randint(1,100);
print(number);
guess = int(input("enter a number"));
while guess!= number:
    if(guess>number):
        print("Lowe number please");
    elif(guess<number):
        print("higher number please");
    guess = int(input("enter a number"));
print("you guessed it right");