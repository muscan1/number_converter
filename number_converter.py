#The role of this program is to convert numbers from decimal to binary, octal, hexadecimal and viceverse
try:
  print("----Welcome to the number converter")
  while True:
    print("Change the number from decimal to binary enter 1")
    print("Change the number from decimal to octal enter 2")
    print("Change the number from decimal to hexadecimal enter 3")
    print("Change Binary to decimal enter 4")
    print("Change Octal to decimal enter 5")
    print("Change Hexidecimal to decimal enter 6")
    print("Enter 7 to exit the program")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            num = int(input("Enter your number: "))
            print(f"{num} in Binary: {bin(num)[2:].zfill(4)}")
        case 2:
            num = int(input("Enter your number: "))
            print(f"{num} in Octal: {oct(num)[2:].zfill(4)}")
        case 3:
            num = int(input("Enter your number:"))
            print(f"{num} in Hexademical:{hex(num)[2:].zfill(4).upper()} ")
        case 4: 
            num = input("Enter Binary number: ")
            print(f"{num} in Decimal: {int(num, 2)}")
        case 5:
            num = input("Enter the octal number: ")
            print(f"{num} in Decimal: {int(num, 8)}")
        case 6:
            num = input("Enter you Hexadecimal number:")
            print(f"{num} in Decimal: {int(num, 16)}")
        case 7:
            print("You are exiting the program")
            break
except ValueError:
  print("Invalid input. Please enter a valid number.")
finally:
  print("Thank you for using this product have a productive day")

