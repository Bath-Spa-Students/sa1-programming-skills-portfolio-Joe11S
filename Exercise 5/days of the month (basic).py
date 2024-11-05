#Exercise 5 = Days of the Month

#Ask user input
month_no = input("Enter Month No: ")

#Month numbers are being listed
months = {
    "1" : "This Month has 31 Days",
    "2" : "This Month has 28 Days",
    "3" : "This Month has 31 Days",
    "4" : "This Month has 30 Days",
    "5" : "This Month has 31 Days",
    "6" : "This Month has 30 Days",
    "7" : "This Month has 31 Days",
    "8" : "This Month has 31 Days",
    "9" : "This Month has 30 Days",
    "10" : "This Month has 31 Days",
    "11" : "This Month has 30 Days",
    "12" : "This Month has 31 Days"
}

#Determine Month

if month_no in months:
    x = months[month_no]
    print(x)
else:
    print("Months cannot go below 0 or above 12")