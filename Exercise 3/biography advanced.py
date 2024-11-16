#Exercise 3 - Biography 

#Take user input of the names
name = input("Enter name: ")
hometown = input("Enter hometown: ")
age = int(input("Enter age: "))

#Define the dictionary of the items in a biography.
biography = {
    "Name" : name,
    "Hometown" : hometown,
    "Age": age
}

#output entries in the biography
print(biography)