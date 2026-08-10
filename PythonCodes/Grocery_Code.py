def main():
    # Intialize the grocery list
    grocery_list = []
    try:
        #Keep taking input until the user signals EOF (Ctrl+D).
        while True:
            grocery_list.append(input())
    except EOFError:
        #Intilize a dictionary to count the occurrences of each item in the grocery list.
        counts = {}
        for item in grocery_list:
            counts[item] = counts.get(item, 0) + 1 #.get(item,0) returns the value for the key 'item' if it exists, otherwise it returns 0 isntead of using an if statement to check if the key exists in the dictionary.  
        for item in sorted(counts): #Sorted is used to sort the keys of the dictionary in alphabetical order.
            print(counts[item], item.upper())

main()
