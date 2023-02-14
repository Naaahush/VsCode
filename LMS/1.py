x =input("Please enter an integer:\n")
#convert str to int
x = int(x)
print(f'You have entered {x}')
if x > 0:
    print("You have entered a positive number")
    if x % 2 == 0:
        print("You have also entered an even number")
        if x >= 10:
            print("This number has multiple digits")
    else:
        print("it's an odd number")
elif x==0:
    print("Lovely choice, 0 is the master of all digits.")
else:
    print("It's a negative number")
    if x % 3 == 0:
        print("This number is divided by 3")
    if x % 2 == 0:
        print("And it's an even number")
    else:
        print("It's an odd number")