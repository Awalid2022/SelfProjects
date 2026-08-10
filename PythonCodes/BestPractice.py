def main():
    plate = input("Plate: ")
    #Instead of checking IF and else on multiple lines, we can use a single line with a conditional expression
    print("Valid" if is_valid(plate) else "Invalid")
    

def is_valid(s):
    #Instead of checking each condition separately, we can combine them into a single return statement for better readability and efficiency
    return (
        2 <= len(s) <= 6
        and s[:2].isalpha()
        and s.isalnum()
        and check_first_num(s)
    )

def check_first_num(s):
    for i, char in enumerate(s):
        '''
        [i:] is used to slice the string and make sure that numbers end till the end not in the middle of the string for example "CS50" is valid but "CS50P" & "CS50P2"is not 
        valid. 
        '''
        if char.isdigit():
            return char != "0" and s[i:].isdigit()
    return True

main()