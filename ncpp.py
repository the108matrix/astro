"""
Number Conversion Practice
"""
import random

print("'##::: ##:::::::'######:::::::'########:::::::'########::")
print(" ###:: ##::::::'##... ##:::::: ##.... ##:::::: ##.... ##:")
print(" ####: ##:::::: ##:::..::::::: ##:::: ##:::::: ##:::: ##:")
print(" ## ## ##:::::: ##:::::::::::: ########::::::: ########::")
print(" ##. ####:::::: ##:::::::::::: ##.....:::::::: ##.....:::")
print(" ##:. ###:'###: ##::: ##:'###: ##::::::::'###: ##::::::::")
print(" ##::. ##: ###:. ######:: ###: ##:::::::: ###: ##::::::::")
print()
print()
print("Welcome to the NUMBER CONVERSION PRACTICE PROGRAM.")
print("To get started, input what you like to practice below.")
print()


numbersystem = ["binary", "hexadecimal", "decimal", "octal"]

selecting = True

while selecting:
    first = input("What Number System you'd like to convert? ")
    
    second = input("What would you like to convert it to? ")
    
    if first == "binary" or first == "hexadecimal" or first == "decimal" or first == "octal" or second == "binary" or second == "hexadecimal" or second == "decimal" or second == "octal":
        print()
        print()
        print()
        print("Okay, let's practice converting", first, "to", second + ".")
        print("Press 'Run' above if you want to reset the program and pick another number conversion")
        break
    else:
        print("Not a valid input. Try again.")
        continue

a = []


running = True

while running:
    for i in range(999):
        a.append(i)
    random.shuffle(a)
    number = a[0]
    

    
    if first == "binary":
        number = (str(bin(number))[2:])
        print("Convert", number, "to", second + ".")
        print()
        print()
        response = int(input("Answer: "))
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    
              

    if first == "decimal":
        number = str(number)
        print("Convert", number, "to", second + ".")
        print()
        print()
        response = int(input("Answer: "))
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    
    
    
    if first == "hexadecimal":
        number = (str(hex(number))[2:])
        print("Convert", number, "to", second + ".")
        print()
        print()
        response = int(input("Answer: "))
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    

    
    if first == "octal":
        number = (str(oct(number))[1:])
        print("Convert", number, "to", second + ".")
        print()
        print()
        response = int(input("Answer: "))
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])


  
    if response == int(answer):
        print("Correct!")
        print()
        print()
    else:
        print("Wrong!")
        print()
        print()


    
    