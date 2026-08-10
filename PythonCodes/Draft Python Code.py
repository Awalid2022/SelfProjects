def addition_function( x , y):

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers (int or float).")
    return x + y

value = addition_function(10,2)
print(f"The total of the addition is equal to : {value}")