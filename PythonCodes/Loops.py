import numpy as np

def main():

    x = 0

    #While loop implementation.
    while x < 3:
        print("Hello")
        x += 1

    #For loop implementaion.
    #Range creates a list from 0 till "n-1"
    for i in  range(3):
        print("Bye")

    #Dict implementation (Key-value data type)
    students = {"Hermione":"Gryffindor",
                "Harry":"Gryffindor",
                "Ron":"Gryffindor",
                }


    for value in students.keys():
        print(value)
main() 