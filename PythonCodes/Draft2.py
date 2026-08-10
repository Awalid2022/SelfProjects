def main():

    Number = int(input("Please Enter a Number : "))
    if bool(Number % 2 == 0) is True and Number > 5 :
        print(f"{Number} is an Even Number and greater than 5")
    elif Number %2 != 0  and Number > 5 :
        print(f"{Number} is an Odd Number and greater than 5")
    
    print("ABC1234"[3:])
main()