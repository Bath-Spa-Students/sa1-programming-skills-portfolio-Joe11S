#Exercise 5 = Days of the Month

#Ask user input
month_no = input("Enter Month No: ")

#Month numbers are being listed
months = {
    "1" : "This Month has 31 Days",
    "2" : "This is February",
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
    check = months[month_no]
    
    #check for leap years
    if check == "This is February":

        #Enter the year input if the month is 2
        year = int(input("Input the Year: "))

        #Check for Leap Years
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("This Month has 29 Days")
                else:
                    print("This Month has 28 Days")
            else:
                print("This Month has 29 Days")
        else:
            print("This Month has 28 Days")
    
    #If the month is not 2
    else:
        print(check)

#a safety measure if months go below 0 or above 12
else:
    print("Months cannot go below 0 or above 12")