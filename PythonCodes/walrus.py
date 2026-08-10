def main():

    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total = 0

    while True:
        try:
            item = input("Item: ")

            # the Walrus operator is an operator ":=" used to assign a value as part of an expression, must be used inside a expression as if statment.
            # simply it executes the expression and assigns it to the variable direclty
            #So in here it got the menu price for the item used , if item isnt founf none is returned from get expression and  assigned to price. then we check the output if isnt none or not.
            if (price := menu.get(item.title())) is not None:
                total = total + price
                print(f"Total: ${total:.2f}")

        except EOFError:
            print()
            break


main()
