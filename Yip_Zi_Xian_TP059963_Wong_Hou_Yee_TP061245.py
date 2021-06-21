# Yip Zi Xian # TP059963
# Wong Hou Yee # TP061245

# First Function
def customerLogin(): # Fuction declared for customer login verification
    print("Please enter your username and password to login.")
    username = str(input("Username: "))
    password = str(input("Password: "))
    
    customer = [] # Empty list
    customer.append(username)
    customer.append(password)
    
    f = open("CustomerUsernamePsw.txt","r") # Open file
    row = f.readlines()

    # Begin loop
    for line in row:
        lines =''.join(line)
        lst = lines.rstrip('\n').split(' | ')

        if lst[0] == customer[0] and lst[1] == customer[1]:
            print('Login Successful. Welcome,', username, '! :)')
            invalid = False
            break
        elif lst[0] != customer[0] or lst[1] != customer[1]:
            invalid = True
    # End loop 

    if invalid:
        customerLogin() # Call back the function if input is wrong
# End function


# Second Function
def interface(): # Declare function for login menu
    print('='*60)
    print('!< WELCOME TO SUPER CAR RENTAL SERVICES ONLINE INTERFACE >!')
    print('='*60)
# Title of the login menu

    print("""
Good day, user!
I am Gabriel, a menu-driven assistant for this online interface.
Although I am not smart, but you will still need to tell me who you are beforehand. :D
    1 - Login as Admin.
    2 - Login as Customer.
    3 - Register as Customer.
    4 - I am just browsing the car for rent.
""")
# Login menu options

    # Begin Loop
    while True: # While loop for input validation
        try:
            inputOption = int(input('Gabriel would kindly like you to introduce yourself first. :D\n'))
        except ValueError:
            print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
            continue 
        else:
            if len(str(inputOption)) != 1 or int(inputOption) > 4: 
                print('Invalid input. Please retype the correct input.')
                continue 
            else:
                int(inputOption)
                break 
        # End Loop

    if inputOption == 1: # Admin login verification
        print('Enter your admin username and password.')
        adminName = str('WY')
        psw = str('1234321')

        username = str(input('Username: '))
        password = str(input('Password: '))

        if (adminName == username) and (psw == password): 
            print('Login Successful. Welcome,', adminName, '! :)')
        else:
            # Begin Loop
            while (adminName != username) or (psw != password):
                print('Either your username or password is incorrect. Please try again. :(')
                username = str(input('Username: '))
                password = str(input('Password: '))
                if (adminName == username) and (psw == password):
                    break 
            print('Login Successful. Welcome,', adminName, '! :)')
            # End Loop

        admin() # Direct to admin main menu

    elif inputOption == 2: # Customer login verification
        
        customerLogin() # Direct to customer login verification 
        customerUse() # Direct to customer main menu after login successful
    
    elif inputOption == 3: # Non-customer registration 
        def registerStep(): # Declare function for registration process
            print('''
Registeration successful. Please fill in your personal information to complete your registeration process.
All your presonal information will be kept private and confidential.
Gabriel will not tell anyone about you. :)
''')
            name = str(input('Name to display: '))
            phone_no = str(input('Phone number: '))

            # Begin Loop
            while len(phone_no) != 10 and len(phone_no) != 11:
                print('Invalid phone format. Please retype.\nMake sure your phone is 10 - 11 numbers long.\n')
                phone_no = str(input('Phone number: '))   
                if len(phone_no) == 10 and len(phone_no) == 11:
                    break
            # End Loop

            card_no = str(input('Card number: '))

            # Begin Loop
            while len(card_no) != 16: 
                print('Invalid card format. Please retype.\nMake sure you card number is 16 numbers long.\n')
                card_no = str(input('Card number: '))  
                if len(card_no) == 16:
                    break
            # End Loop

            individualFile = open('Customer_Details.txt', 'a') # Open file

            cusDetail = [name, phone_no, card_no]

            individualFile.write(' | '.join(cusDetail))
            individualFile.write('\n')

            individualFile.close() # Close file
            print('Your customer details have successfully saved. Please proceed to login for more functions.')
        # End function

        print('Please register in order to access other customer functions.')
        username = str(input("Username: "))
        password = str(input("Password: "))
        
        f = open("CustomerUsernamePsw.txt", "r") # Open file
        info = f.read()
        if username not in info: 
            f = open("CustomerUsernamePsw.txt", "a") # Change file mode

            cusUserPsw = [username, password]

            f.write(' | '.join(cusUserPsw))
            f.write("\n")

            f.close() # Close file

            registerStep() # Direct to registration process
        
        else:
            # Begin Loop
            for line in f:
                lst = line.split(" | ")
                if lst[0] == username:
                    break
            # End Loop

            # Begin Loop
            while True: 
                print("Username already taken. Please try another username. :(")
                username = str(input("Username: "))
                password = str(input("Password: "))
                
                f = open("CustomerUsernamePsw.txt", "r") # Open file
                info = f.read()
                if username not in info:
                    break
                f.close() # Close file
            # End Loop

            f = open("CustomerUsernamePsw.txt", "a") # Open file

            cusUserPsw = [username, password]

            f.write(' | '.join(cusUserPsw))
            f.write("\n")
            
            f.close() # Close file
        
            registerStep() # Direct to registration process

        interface() # Direct to login menu

    elif inputOption == 4: # Display all car for rent details for all users
        readFile = open('Car_Details.txt', 'r') # Open file
        displayFile = readFile.read()
        print(displayFile)
        readFile.close() # Close file

        interface() # Direct to login menu
# End function


# Third function
def admin(): # Declare function for admin main menu
    print("""
Gabriel at your service. How can I kindly help you?
Please select the function below so that I know what you want me to do. :)\n
    1 - Add Car for Rent
    2 - Modify Car Details
    3 - Display Customer Rental Records
    4 - Search for a specific record
    5 - Return a Rented Car
    6 - Search Engine
    7 - Exit
""")

    # Begin Loop
    while True: # While loop for data validation
        try:
            adminInput = int(input('Gabriel awaiting your order. :D\n'))
        except ValueError:
            print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
            continue 
        else:
            if len(str(adminInput)) != 1 or int(adminInput) > 7:
                print('Invalid input. Please retype the correct input.')
                continue 
            else:
                int(adminInput)
                break 
    # End Loop

    if adminInput == 1: # Add new car for rent

        # Fourth function
        def category(): # Declare function to include table category while adding 
            categoryCar = ['Code', 'Car Brand', 'Rent Price per day (RM)', 'Availability for Rent']

            # Begin Loop
            while True: # While loop for data validation
                try: 
                    inputCategory = int(input('''
Do you want Gabriel to insert the category for your table? :D
    1 - Yes, please.
    2 - No, thank you.
    3 - You can still go back to the menu.
'''))
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(inputCategory)) != 1 or int(inputCategory) > 3:
                        print('Invalid input. Please retype the correct input.')
                        continue 
                    else:
                        int(inputCategory)
                        break 
            # End Loop

            if inputCategory == 1: # Add category
                add_car = open('Car_Details.txt', 'a') # Open file
                add_car.write(' | '.join(categoryCar))
                add_car.write('\n')
                add_car.close() # Close file

            elif inputCategory == 2: # Not adding category
                pass # Ignore and skip the process

            elif inputCategory == 3: # Back to admin main menu
                admin() # Direct to admin main menu
        # End function

        # Begin Loop
        while True: # While loop for data validation
            amount = input('How many cars you want to add?\nExample: 6\n')
            try:
                amount = int(amount)
                break 
            except:
                print('Please enter a specific NUMBER of cars to add.')
        # End Loop

        # Begin Loop
        for i in range(0, amount+1):
            if i == 0:
                category() # Direct to adding category options
            else:
                # Begin Loop
                while True: # While loop for data validation
                    code = str(input('''
Enter the car types followed by the code number assigned.
    SDN - Sedan
    SUV - Sport Utility Vehicles
    HBK - Hatchback
    MVN - Minivan
    (Example: SDNxxx)
'''))
                    if len(code) != 6:
                        print('''
Invalid input format. Please retype.
Make sure it starts with the code followed by the code number.
''')
                        continue 
                    else:
                        break 
                # End Loop

                # Begin Loop
                while True: # While loop for data validation
                    car_brand = str(input('Enter the car brand.\nExample: Honda Accord\n'))
                    if len(car_brand) <= 5:
                        print('Please enter an invalid car brand.')
                        continue 
                    else:
                        break
                # End Loop

                # Begin Loop
                while True: # While loop for data validation
                    price_per_day = str(input('Enter the price for rent.\nExample: xxx\n'))
                    if len(price_per_day) != 3:
                        print('The range of price is RM100-RM999. Please retype a valid price.')
                        continue 
                    else:
                        break 
                # End Loop

                car_availability = str(input('Is the car ready for rent?\nExample: Yes/No\n'))
                # Begin Loop
                while car_availability != 'Yes' and car_availability != 'No':
                    car_availability = str(input('Is the car ready for rent?\nExample: Yes/No\n'))
                    if car_availability == 'Yes' or car_availability == 'No':
                        break
                # End Loop

                add_car = open('Car_Details.txt', 'a') # Open file

                data = [code, car_brand, price_per_day, car_availability]
                add_car.write(' | '.join(data))
                add_car.write('\n')

                add_car.close() # Close file

                print(data) # Display data of new car for rent added
        # End Loop
        admin() # Direct to admin main menu
    
    elif adminInput == 2: # Modify existing car details
        readFile = open('Car_Details.txt', 'r') # Open file
        displayFile = readFile.read()
        print(displayFile) 
        readFile.close() # Close file
        
        readFile = open('Car_Details.txt', 'r') # Open file
        lst = [] # Empty list

        # Begin Loop
        for i in readFile:
            j = i.strip('\n') 
            k = j.split(' | ') 
            lst.append(k)
        # End Loop

        # Begin Loop
        while True: # While loop for data validation
            try:
                inputCode = int(input('''
Enter which code you wish to modify?
Example: 1-20
'''))
                try:
                    print(lst[inputCode])
                except IndexError:
                    print('There is no such car in the database.')
                    continue 
                
            except ValueError:
                print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                continue 
            else:
                if len(str(inputCode)) > 3:
                    print('Invalid code. Code should be at most 3 numbers. Please retype.\n')
                    continue 
                else:
                    int(inputCode)
                    break 
        # End Loop

        # Begin Loop
        while True: # While loop for data validation
            try: 
                inputIndex = int(input('''
Which section do you want to modify?                    
    0 - Code
    1 - Car Brand
    2 - Rent Price per day (RM)
    3 - Availability for Rent
    4 - Wrong code? Back to Menu.
'''))
            except ValueError:
                print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                continue 
            else:
                if len(str(inputIndex)) != 1 or int(inputIndex) > 4:
                    print('Invalid input. Please retype.')
                    continue 
                else:
                    int(inputIndex)
                    break 
        # End Loop

        if inputIndex == 4: # Back to admin main menu
            admin() # Direct to admin main menu
        else:
            print(lst[inputCode][inputIndex])

            temp = str(input('Enter the new data to replace the old data.\n')) 
            print(temp)

            lst[inputCode][inputIndex] = temp # Replace old data with new data
            print(lst)

            writeFile = open('Car_Details.txt', 'w') # Open file

            # Begin Loop
            for i in lst:
                writeFile.write(' | '.join(i)+'\n')
            # End Loop
            writeFile.close() # Close file
            
        admin() # Direct to admin main menu

    elif adminInput == 3: # View all customer rental history records
        historyFile = open('Rental_History_Records.txt', 'r') # Open file
        showHisFile = historyFile.read()
        print(showHisFile)
        historyFile.close() # Close file

        admin() # Direct to admin main menu

    elif adminInput == 4: # View specific customer rental history records via customer username input
        print('''
Gabriel will help you to find the customer you specified.
Just tell Gabriel the username of the customer.
Gabriel will display all his or her rental records.
''')
        tempInput = str(input())

        hisReadFile = open('Rental_History_Records.txt', 'r') # Open file
        hlst = [] # Empty list

        # Begin Loop
        for i in hisReadFile:
                j = i.strip('\n') 
                k = j.split(' | ') 
                hlst.append(k)
        # End Loop

        # Begin Loop
        for i in hlst:
            if i[0] == tempInput:
                print(i) # Display records according to required username
        # End Loop
        print('Above is/are the rental record(s) of', tempInput)
        print('If it is empty, it means the customer does not exist or have not rent a car before')
        
        admin() # Direct to admin main menu

    elif adminInput == 5: # Return a rented car from customer
        readFile = open('Car_Details.txt', 'r') # Open file
        lst = [] # Empty list

        # Begin Loop
        for i in readFile:
            j = i.strip('\n') 
            k = j.split(' | ') 
            lst.append(k)
        # End Loop

        # Begin Loop
        for i in lst:
            if i[-1] == 'No':
                print(i) # Display rented car only
        # End Loop

        # Begin Loop
        while True: # While loop for data validation
            try:
                inputCode = int(input('''
Enter which code you wish to modify?
Example: 1-20
'''))
                try:
                    print(lst[inputCode])
                except IndexError:
                    print('There is no such car in the database.')
                    continue 
                
            except ValueError:
                print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                continue
            else:
                if len(str(inputCode)) >= 3:
                    print('Invalid code. Code should be at most 3 numbers. Please retype.')
                    continue
                else:
                    int(inputCode)
                    break 
        # End Loop

        temp = str(input('Type Yes to return the car.\nType No to remain the car at rented.\n'))
        while temp != 'No' and temp != 'Yes': 
            temp = str(input('Type Yes to return the car.\nType No to remain the car at rented.\n'))
            print('Either Yes or No. Please do not type other input.')
            if temp == 'No' or temp == 'Yes':
                break 

        lst[inputCode][3] = temp # Replace old data with new data

        print(lst[inputCode])

        if temp == 'Yes':
            print('The respective car is successfully returned and wating for another rental.')
        elif temp == 'No':
            print('The respective car is still remain at rented.')

        writeFile = open('Car_Details.txt', 'w') # Open file

        # Begin Loop
        for i in lst:
            writeFile.write(' | '.join(i)+'\n')
        # End Loop

        writeFile.close() # Close file
        admin() # Direct to admin main menu

    elif adminInput == 6: # Search engine for admin
        readFile = open('Car_Details.txt', 'r') # Open file
        lst = [] # Empty list

        # Begin Loop
        for i in readFile:
            j = i.strip('\n')
            k = j.split(' | ')
            lst.append(k)
        # End Loop

        print('''
Yes? How can Gabriel help you to display the data?
    1 - Car Types
    2 - Car Availability
    3 - Customer Bookings for a specific timeframe
    4 - Back to menu
''')

        # Begin Loop
        while True: # While loop for data validation
            try:
                inputDisplay = int(input())
            except ValueError:
                print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                continue 
            else:
                if len(str(inputDisplay)) != 1 or int(inputDisplay) > 4:
                    print('Invalid input. Please retype.')
                    continue 
                else:
                    int(inputDisplay)
                    break 
        # End Loop

        if inputDisplay == 1: # Search car types
            print('''
What types of car are you looking for?
    1 - Sedan (SDN)
    2 - Sport Utility Vehicle (SUV)
    3 - Hatchback (HBK)
    4 - Minivan (MVN)
''')

            # Begin Loop
            while True: # While loop for data validation
                try:
                    inputTypes = int(input())
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(inputTypes)) != 1 or int(inputTypes) > 4:
                        print('Invalid input. Please retype.')
                        continue 
                    else:
                        int(inputTypes)
                        break 
            # End Loop

            if inputTypes == 1:
                for i in lst:
                    if i[0].startswith('SDN'):
                        print(i)
            elif inputTypes == 2:
                for i in lst:
                    if i[0].startswith('SUV'):
                        print(i)
            elif inputTypes == 3:
                for i in lst:
                    if i[0].startswith('HBK'):
                        print(i)
            elif inputTypes == 4:
                for i in lst:
                    if i[0].startswith('MVN'):
                        print(i)

            admin() # Direct to admin main menu

        elif inputDisplay == 2: # Search car availability
            print('''
You are looking car available for rent or car that already rented out?
    1 - Available
    2 - Rented Out
''')

            # Begin Loop
            while True: # While loop for data validation
                try:
                    inputAvailability = int(input())
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(inputAvailability)) != 1 or int(inputAvailability) > 2:
                        print('Invalid input. Please retype.')
                        continue 
                    else:
                        int(inputAvailability)
                        break 
            # End Loop

            if inputAvailability == 1:
                for i in lst:
                    for element in i:
                        if element == 'Yes':
                            print(i)
            elif inputAvailability == 2:
                for i in lst:
                    for element in i:
                        if element == 'No':
                            print(i)

            admin() # Direct to admin main menu
            
        elif inputDisplay == 3: # Search rental history records according to month
            historyFile = open('Rental_History_Records.txt', 'r') # Open file
            hlst = [] # Empty list

            # Begin Loop
            for i in historyFile:
                j = i.strip('\n')
                k = j.split(' | ')
                hlst.append(k)
            # End Loop

            # Begin Loop
            while True: # While loop for data validation
                try:
                    inputMonth = int(input('''
Which month of customer rental records you wish to display?
January (1) - December (12)
Please enter in numeric form.
'''))
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(inputMonth)) > 2 or int(inputMonth) > 12:
                        print('There is at most two digits for a month. <O.O> Where are you living?')
                        continue 
                    else:
                        int(inputMonth)
                        break 
            # End Loop

            a = str(inputMonth)
            b = a.zfill(2) # Fill spaces in front of 1 - 9 with one zero to match the date format

            try:
                for x in hlst:
                    if b == (x[4][5:7]):
                        print(x)
            except IndexError:
                pass # Ignore error

            admin() # Direct to admin main menu

        elif inputDisplay == 4: # Back to admin main menu
            admin() # Direct to admin main menu
    
    elif adminInput == 7: # Logout from admin
        def exit_function(): # Declare function for logging out
            print('Exit this program?')

            bye = str(input('Yes or No? \n'))
            while bye != 'Yes' and bye != 'No': 
                bye = str(input('Yes or No? \n'))
                if bye != 'Yes' or bye != 'No':
                    break 

            Y = str('Yes')
            N = str('No')

            if bye == Y:
                print('You are always welcome. Have a nice day.')
                interface() # Direct to login menu
            elif bye == N:
                print('Well, do you still have anything that I can help? :).')
                admin() # Direct to admin main menu
            else:
                print('Uh? What did you type? ._." I did not understand.')
                exit_function() # Direct to exit option

        exit_function() # Call function for logging out
# End function


# Fifth fuction
def customerUse(): # Declare function for customer main menu
    print("""
Gabriel at your service. How can I kindly help you?
Please select the function below so that I know what you want me to do. :)\n
    1 - Modify Personal Details
    2 - View Personal Rental History
    3 - View Car Details List
    4 - Book a Car and Make Payment
    5 - Exit
""")

    # Begin Loop
    while True: # While loop for data validation
        try:
            customerInput = int(input('Gabriel awaiting your order. :D\n'))
        except ValueError:
            print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
            continue 
        else:
            if len(str(customerInput)) != 1 or int(customerInput) > 5:
                print('Invalid input. Please retype.')
                continue 
            else: 
                int(customerInput)
                break 
    # End Loop

    if customerInput == 1: # Modify personal details exclude username and password

        print("Please enter your username and password to verify")
        username = str(input("Username: "))
        password = str(input("Password: "))

        credential = username + " | " + password + "\n"

        f = open("CustomerUsernamePsw.txt","r") # Open file
        line = f.readlines()
        no_line = len(line)
        count = 0
        x = 0

        # Begin Loop
        while x <= no_line:
            try:
                if line[count] == credential:
                    break
                count = count + 1
            except IndexError:
                print('Either your username or password is incorrect. Please try again.')
                customerUse() # Direct to customer main menu
        # End Loop
        f.close() # Close file
        
        lst = [] # Empty list
        readFile = open("Customer_Details.txt","r") # Open file

        # Begin Loop
        for i in readFile:
            j = i.strip("\n") 
            k = j.split(' | ') 
            lst.append(k)
        # End Loop

        print(lst[count])

        # Begin Loop
        while True: # While loop for data validation
            try: 
                option = int(input('''
Which section do you wish to modify
    0 - Name
    1 - Phone Number
    2 - Card Number 
    3 - Back to Menu 
'''))
            except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
            else:
                if len(str(option)) != 1 or int(option) > 4:
                    print('Invalid input. Please retype.')
                    continue 
                else:
                    int(option)
                    break 
        # End Loop

        if option == 3: # Back to customer main menu
            customerUse() # Direct to customer main menu
        else:
            if option == 0: # Change display name
                temp = str(input("Please enter your new display name: "))
                lst[count][option] = temp

            elif option == 1: # Change phone number
                temp = str(input('Example: 012xxxxxxx or 011xxxxxxxx\nNew Phone number: '))
                # Begin Loop
                while len(temp) != 10 and len(temp) != 11: 
                    print('Invalid phone format. Please retype.\nMake sure your phone is 10 - 11 numbers long.\n')
                    temp = str(input('New Phone number: '))   
                    if len(temp) == 10 and len(temp) == 11:
                        break 
                # End Loop
                lst[count][option] = temp

            elif option == 2: # Change card number
                temp = str(input('Example: 5839xxxx1622xxxx\nNew Card number: '))
                # Begin Loop
                while len(temp) != 16: 
                    print('Invalid card format. Please retype.\nMake sure you card number is 16 numbers long.\n')
                    temp = str(input('New Card number: '))  
                    if len(temp) == 16: 
                        break 
                # End Loop
                lst[count][option] = temp
                
        writeFile = open("Customer_Details.txt","w") # Open file
        # Begin Loop
        for i in lst:
            writeFile.write(' | '.join(i)+'\n')
        # End Loop
        writeFile.close() # Close file
            
        print(lst[count])
        print('Modification Successful.')

        customerUse() # Direct to customer main menu
            
    elif customerInput == 2: # View all personal rental history records
        username = str(input('''
Gabriel will need to know your username in order to find your rental history records.
Please kindly type your username.
'''))
        individualFile = open("Rental_History_Records.txt", "r") # Open file
        # Begin Loop
        for x in individualFile:
            lst = x.split(' | ')
            if lst[0] == username:
                print(x)
        # End Loop
        individualFile.close() # Close file

        print('Here is your rental history records,', username)
        print('''
If it is empty, it means you have not rent any car yet.
Or maybe you typed your username wrongly.
''')
        customerUse() # Direct to customer main menu
        
    elif customerInput == 3: # View all car for rent details
        readFile = open('Car_Details.txt', 'r') # Open file
        displayFile = readFile.read()
        print(displayFile) 
        readFile.close() # Close file
        
        customerUse() # Direct to customer main menu
        
    elif customerInput == 4: # Book, rent a car and confirm payment
        from datetime import datetime # Import datetime in order to record the actual date and time
        from datetime import timedelta # Import timedelta in order to add duration to datetime
    
        date_and_time = datetime.now().replace(microsecond=0) # Format time to be shown in readable format (yyyy-mm-dd hh:mm:ss)

        def bookCar(): # Declare function for car booking process
            readFile = open('Car_Details.txt', 'r') # Open file
            lst = [] # Empty list

            # Begin Loop
            for i in readFile:
                j = i.strip('\n') 
                k = j.split(' | ') 
                lst.append(k)
            # End Loop

            # Begin Loop
            for i in lst:
                for element in i:
                    if element.startswith('Y'):
                        print(i)
            # End Loop

            print("Please select your desired car for rent by typing the code according to the menu.\nExample: SDNxxx")
            code = str(input())

            readFile = open("Car_Details.txt","r") # Open file
            car_count = 0
            
            # Begin Loop
            for row in readFile:
                line = row.strip("\n")
                lines = line.split(" | ")
                if lines[0] == code:
                    break 
                car_count = car_count + 1
            # End Loop

            # Begin Loop
            while True: # While loop for data validation
                try:
                    duration = int(input('''
How many days you like to rent this car for?
Maximum day for rent is 30 days.
NOTE: Rent price is counted as per day. Any wrong input Gabriel will not entertain. :D
'''))
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(duration)) > 2 or int(duration) > 30:
                        print('Please note that you can only rent at most 30 days.')
                        continue 
                    else:
                        break 
            # End Loop

            carFile = open("Car_Details.txt","r") # Open file
            rows = carFile.readlines()

            # Begin Loop
            while True: # While loop for data validation
                try:
                    car = rows[car_count]
                except IndexError:
                    print('''
The car code you enter does not exist.
Gabriel took you back to the menu to avoid any mistaken rental. :D
''')
                    customerUse() # Direct to customer main menu
                else:
                    break
            # End Loop

            print('The car you requested to rent is\n',car ,'The duration you requested is\n',duration ,' day(s)')

            # Begin Loop
            while True: # While loop for data validation
                try:
                    confirmation = int(input('''
Are you sure?
1 - Yes
2 - No
'''))
                except ValueError:
                    print('Gabriel do not understand what are you saying. Please type as per the menu give. :(')
                    continue 
                else:
                    if len(str(confirmation)) != 1 or int(confirmation) > 2:
                        print('Invalid input. Please retype.')
                        continue 
                    else:
                        int(confirmation)
                        break 
            # End Loop

            if confirmation == 1: # Confirm to book
                lst = car.split(" | ")
                price = lst[2]
                integer = price.strip()
                rentPrice = int(integer)
                
                amount = rentPrice * duration # Calculate total amount to pay
                new_time = date_and_time + timedelta(days=duration) # Calculate the date to return back the rented car
                
                print("Total amount to pay: ", "RM ",amount)

                print("Please enter your username and password for confirmation.")
                username = str(input("Username: "))
                password = str(input("Password: "))
                customer = username + ' | ' + password + '\n'

                f = open("CustomerUsernamePsw.txt","r") # Open file
                line = f.readlines()
                no_line = len(line)
                count = 0
                x = 0

                # Begin Loop
                while x <= no_line:
                    try:
                        if line[count] == customer:
                            break
                        count = count + 1
                    except IndexError:
                        print('Either your username or password is incorrect. Please try again.')
                        print('Gabriel will void this order to prevent any troublesome matters.')
                        customerUse() # Direct to customer main menu
                # End Loop

                f.close() # Close file

                f = open("CustomerUsernamePsw.txt","r") # Open file
                row = f.readlines()
                if customer in row:
                    print("Verification Successful")
                else:
                    # Begin Loop
                    while True: # While loop for data validation
                        print("Either your username or password is incorrect. Please try again")
                        username = str(input("Username: "))
                        password = str(input("Password: "))
                        customer = username + ' | ' + password + '\n'
                        if customer in row:
                            break
                    print("Verification Successful")
                    # End Loop
                f.close() # Close file
                        
                print('Please type your card number to make the payment.')
                card_no = str(input('Example: 2487xxxx1523xxxx\nCard number: '))

                # Begin Loop
                while len(card_no) != 16: # While loop for data validation
                    print('Invalid card format. Please retype. Make sure your card number is 16 numbers long.')
                    card_no = str(input('Card number: '))  
                    if len(card_no) == 16:
                        break
                # End Loop

                lst = [] # Empty list
                readFile = open("Customer_Details.txt","r") # Open file

                # Begin Loop
                for i in readFile:
                    j = i.strip("\n") 
                    k = j.split(' | ') 
                    lst.append(k)
                # End Loop

                if card_no == lst[count][2]:
                    print('Your booking has confirmed! Booking time is ',date_and_time)
                    print('Please kindly return your rented car by ',new_time)
                else:
                    print('Invalid card number. Make sure you typed correctly.')
                    card_no = str(input('Example: 6284xxxx2346xxxx\nCard Number: '))

                    # Begin Loop
                    while len(card_no) != 16: 
                        print('Invalid card format or wrong card number. Please retype. Make sure your card number is 16 numbers long.')
                        if len(card_no) == 16:
                            if card_no == (line[count])[2]:
                                break 
                    # End Loop

                    print('Your booking has confirmed! Booking time is ',date_and_time)
                    print('Please kindly return your rented car by ',new_time)

                historyFile = open('Rental_History_Records.txt', 'a') # Open file
                templst = [username, 'Rented Car Code', code, 'Booking Time', date_and_time, 'Duration (day(s))', duration, 'Return Before', new_time ]
                
                # Begin Loop
                for i in templst:
                    historyFile.write(str(i)+' | ')
                historyFile.write('\n')
                # End Loop

                historyFile.close() # Close file

                readFile = open('Car_Details.txt', 'r') # Open file
                lst = [] # Empty list

                # Begin Loop
                for i in readFile:
                    j = i.strip('\n') 
                    k = j.split(' | ') 
                    lst.append(k)
                # End Loop

                temp = 'No'
                (lst[car_count])[3] = temp # Replace old data with new data

                writeFile = open('Car_Details.txt', 'w') # Open file
                # Begin Loop
                for i in lst:
                    writeFile.write(' | '.join(i)+'\n')
                # End Loop
                writeFile.close() # Close file

                customerUse() # Direct to customer main menu

            elif confirmation == 2: # Cancel booking
                print('Booking process cancelled. Gabriel took you back to the menu. :)')
                customerUse() # Direct to customer main menu
   
        bookCar() # Call function for car booking process
        
    elif customerInput == 5: # Logout from customer
        def exit_function(): # Declare function for logging out
            print('Exit this program?')

            bye = str(input('Yes or No? \n'))
            while bye != 'Yes' and bye != 'No':
                bye = str(input('Yes or No? \n'))
                if bye != 'Yes' or bye != 'No':
                    break 
                
            Y = str('Yes')
            N = str('No')

            if bye == Y:
                print('You are always welcome. Have a nice day.')
                interface() # Direct to login menu
            elif bye == N:
                print('Well, do you still have anything that I can help? :).')
                customerUse() # Direct to customer main menu
            else:
                print('Uh? What did you type? ._." I did not understand.')
                exit_function() # Direct to exit options

        exit_function() # Call functionn to logout
        
interface() # Call function to start running the program