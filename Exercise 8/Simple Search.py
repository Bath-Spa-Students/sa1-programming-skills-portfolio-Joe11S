#list down all the names.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#ask for user input
search_input = input("Search for your name: ")

#search for list and find the name in it
if search_input in names:
    print(search_input, "is in the list of names.")
else:
    print(search_input, "not found.")

