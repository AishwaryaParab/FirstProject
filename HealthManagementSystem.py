def logdata(name, activity):
    if name == 1:
        if activity == 1:
            fp = open("AishwaryaFood.txt", "a")
            meal = input("Enter your meal: ")
            date = getdate()         
            fp.write(str([str(date)])+ ":" + meal+ "\n")
            fp.close()
        elif activity == 2:
            fp = open("AishwaryaExer.txt", "a")
            workout = input("Enter your workout: ")
            date = getdate()
            fp.write(str([str(date)])+ ":" + workout + "\n")
            fp.close()
        else:
            print("Invalid statement. Try Again!")
    elif name == 2:
        if activity == 1:
            fp = open("ShridharFood.txt", "a")
            meal = input("Enter your meal: ")
            date = getdate()
            fp.write(str([str(date)])+ ":" + meal + "\n")
            fp.close()
        elif activity == 2:
            fp = open("ShridharExer.txt", "a")
            workout = input("Enter your workout: ")
            date = getdate()
            fp.write(str([str(date)])+ ":" + workout + "\n")
            fp.close()
        else:
            print("Inavlid statement. Try Again!")
    elif name == 3:
        if activity == 1:
            fp = open("RohitFood.txt", "a")
            meal = input("Enter your meal: ")
            date = getdate()
            fp.write(str([str(date)])+ ":" + meal + "\n")
            fp.close()
        elif activity == 2:
            fp = open("RohitExer.txt", "a")
            workout = input("Enter your workout: ")
            date = getdate()
            fp.write(str([str(date)])+ ":" + workout + "\n")
            fp.close()
        else:
            print("Inavlid statement. Try Again!")
    else:
            print("Inavlid statement. Try Again!")
    
    

def retrievedata(name, activity):
    if name == 1:
        if activity == 1:
            fp = open("AishwaryaFood.txt", "r")
            print(fp.read())
            fp.close()
        elif activity == 2:
            fp = open("AishwaryaExer.txt", "r")
            print(fp.read())
            fp.close()
    elif name == 2:
        if activity == 1:
            fp = open("ShridharFood.txt", "r")
            print(fp.read())
            fp.close()
        elif activity == 2:
            fp = open("ShridharExer.txt", "r")
            print(fp.read())
            fp.close()
    elif name == 3:
        if activity == 1:
            fp = open("RohitFood.txt", "r")
            print(fp.read())
            fp.close()
        elif activity == 2:
            fp = open("RohitExer.txt", "r")
            print(fp.read())
            fp.close()
    else:
        print("Inavlid statement. Try Again!")

def again():
    choice = input("Do you want to continue- Yes or No: ")
    if choice == "Yes":
        health()
    else:
        print("Thank you!")

def getdate():
    import datetime
    return datetime.datetime.now()

def health():  
    date = getdate()
    print("Entry on ", date)
    print("Do you want to log or retrieve data: \n")
    ch = int(input("1 - Log \n2 - Retrive \n"))
    if ch == 1:
        print("Whose data do you want to log:\n")
        name1 = int(input("1 - Aishwarya \n2 - Shridhar\n3 - Rohit\n"))
    elif ch == 2:
        print("Whose data do you want to retrieve:\n")
        name2 = int(input("1 - Aishwarya \n2 - Shridhar\n3 - Rohit\n"))    
    print("Food or Exercise?\n")
    course = int(input("1 - Food\n2 - Exercise\n"))

    if ch == 1:
        logdata(name1, course)
    elif ch == 2:
        retrievedata(name2, course)
    else: 
        print("Invalid statement. Try Again!")    
    again()

print("Welcome to our Health Management System!")
health()
