import string
import hashlib
import statistics
licence_char = "aannnnnn" #characters of the licence a = letter n = numbers
licence_correct_length = len(licence_char) #gets length of licence_char to find the length licence plate should be 
speed_brackets = [30,110] #range of valid speed limts
using_program = True #for checking that user is still using program
TABLE_MIN_LENGTH_UNITS = 16 #specifies the length of a cell in the table
#values that are going to be put on the header of a table
header_row = ["Driver","Licence","Limit (km/h)","Speed (km/h)","Over Limit (km/h)","Fine ($)",]
cell_length = TABLE_MIN_LENGTH_UNITS+1 # specifies the length of a single cell
speed_fines = { #specifies the fines you get for each speeding limit
    30:[1,10],
    80:[11,20],
    170:[21,30],
    400:[31,40],
    620:[41,999999999999],
}

#below is a hash of the password: testingpassword
#NOTE COMMENT ABOVE WOULD NOT BE SHOWN IF THIS WAS A REAL PROGRAM HOWEVER
#SINCE THIS IS FOR SCHOOL THE PASSWORD IS ADDED SO THE MARKER KNOWS HOW TO ENTER THE
#DATABASE INSTEAD OF BEING STUCK.
#this is hashed so a criminal inspecting the code can't easily find the password
#hash is in sha 256
database_password = "9cf7d77d7bec9aa0ad492029e667720b5cc18c1eff1928a145ba6d96c5e7530a"
incorrect_password = True

#the speeding record database
speeding_records = [
    {"driver": "John Smith", "licence":"AB123456","limit":50,"speed":68 },
    {"driver": "Timmy Johnes", "licence":"SS676767","limit":32,"speed":67 }
]

#the list of wanted people
wanted_list = [
    "Dummy Egg",
    "Wanted Person",
    "Wanted Human",
    "Wanted Entity",
    "I Wanted",
]

def warrent_check(name):
    '''checks the name in the wanted list and creates a warning if it is in it'''
    if name in wanted_list:
        print("*********************************")
        print("  •   •     ••••• ••••  •••••")
        print(" • •  •     •     •   •   •")
        print("••••• •     ••••  ••••    •")
        print("•   • •     •     •  •    •")
        print("•   • ••••• ••••• •   •   •")
        print("*********************************")
        print(f"Driver '{name}' is a wanted person")
        print("*********************************")
    
def print_header():
    '''prints the header of the data for tables'''
    print("|".join(f"{str(unit):>{TABLE_MIN_LENGTH_UNITS}}" for unit in header_row))
    print(cell_length*6*"-")


def print_record(driver,licence,limit,speed):
    '''gets data and prints out a single record'''
    #calcuates varibles like over limit and fine to reduce amount of parameters 
    over_limit = speed-limit
    fine = cal_speed_fine(speed,limit)
    
    single_record = [] #list for data to be printed into a table
    
    
    
    #formats the records into a list for printing into a table
    single_record.append(driver)
    single_record.append(licence)
    single_record.append(limit)
    single_record.append(speed)
    single_record.append(over_limit)
    single_record.append(fine)

    #prints the record in a table format
    print("|".join(f"{str(unit):>{TABLE_MIN_LENGTH_UNITS}}" for unit in single_record))
    #prints a divider so it's easier to see the cells
    print(cell_length*6*"-")


def add_to_record(driver,licence,limit,speed):
    '''adds a driver to the record'''
    #formats a dictionary to be appended into speeding records
    formated_dict = {"driver": driver, "licence":licence,"limit":limit,"speed":speed }
    #adds the fromated dict

    speeding_records.append(formated_dict)
    print("Successfully added record")

def valid_name(name):
    '''checks if name is valid'''
    # strips spaces
    n_space_name = name.replace(" ","")
    #checks if name is fully alphabet and doesn't have numbers
    if n_space_name.isalpha():
        print("name added successfully")
        return True
    else:
        print("Name can't be blank or have non alphabet characters")
        return False

def licence_valid(licence):
    '''Checks if the licence is valid '''
    licence_length = len(licence) # gets length of licence that was inputed
    licence.replace(" ","") # removes spaces
    if licence_length == licence_correct_length:
        for i in range(0,licence_length):
            #checks if the letter is to be a alphabate or number
            #and check it with the user's licence
            if licence_char[i] == "a":
                if not licence[i].isalpha():
                    #tells the user what type of character should that one be and gives the format
                    print(f"Character {i+1} must be a alphabet ")
                    print(f"licence must be in {licence_char} format ")
                    print(f"where 'a' stands for alpha and 'n' for number")
                    print(" ")
                    return False
            elif licence_char[i] == "n":
                if not licence[i].isdigit():
                    #tells the user what type of character should that one be and gives the format
                    print(f"Character {i+1} must be a number ")
                    print(f"licence must be in {licence_char} format ")
                    print(f"where 'a' stands for alpha and 'n' for number")
                    print(" ")
                    return False
        print("Pass checks licence is valid")
        print(" ")
        return True
    else:
        print(f"licence must be {licence_correct_length} characters long")
        print(" ")
        return False


def speed_valid(speed):
    '''checks if speed is a valid range and returns true or false'''
    #checks the speed in the speeing brackets list
    if speed in range(speed_brackets[0],speed_brackets[1]+1):
        print("speed success added")
        return True
    else:
        #tells the user what speed the speed must be in
        print(f"speed must be in between {speed_brackets[0]} and {speed_brackets[1]} ")
        return False

def cal_speed_fine(speed,speed_limit):
    '''cals the speed fine based on how over the limit they are'''
    speed_over = speed-speed_limit
    #checks all the speeding brackets in speed_fines to see what fine is
    #approprate for their speed
    for i in speed_fines:
        if speed_over in range(speed_fines[i][0],speed_fines[i][1]+1):
            return i


def create_record():
    '''creates a speeding offence'''
    print("-------------------------------")

    print("")
    #Gets the driver name
    driver_name = input("Input driver name: ")
    # if name isn't valid asks the user to input the name correctly until they do
    while not valid_name(driver_name):
        driver_name = input("Please input driver name correctly: ")

    print("")
    #Gets the driver licence 
    driver_licence = input("Input driver licence: ")
    # if licence isn't valid a
    # sks the user to input the licence correctly until they do
    while not licence_valid(driver_licence):
        driver_licence = input("Please input driver licence correctly: ")

    print("")

    valid_speed = False
    # if name isn't valid asks the user to input the name correctly until they do
    while not valid_speed:
        #try to prevent int errors when the user inputs a string
        try:
            speed_limit = int(input(f"Input speed limit {speed_brackets[0]} and {speed_brackets[1]}: "))
            if speed_valid(speed_limit):
                valid_speed = True
        except: 
            print("Only input numbers")

    print("")
    driver_speed = 0
    # checks if the driver is above the speed limit and rejects the request if it isn't
    while driver_speed <= speed_limit:
        #try to prevent int errors when the user inputs a string
        try:
            driver_speed = int(input("Input driver speed: "))
            if driver_speed <= speed_limit:
                print("no speeding offence has occured in this speed input a correct speed")
        except: 
            print("Only input numbers")

    driver_name = driver_name.strip().title() # formats the driver name to be in title case and removes excess spaces.
    driver_licence = driver_licence.upper() # formats the driver licence to be in full uppercase
    #adds the record to the database
    add_to_record(driver_name,driver_licence,speed_limit,driver_speed)
    print("")
    #prints the record
    print_header()
    print_record(driver_name,driver_licence,speed_limit,driver_speed)
    #checks the driver name for a wanted list and warns the driver if it is
    warrent_check(driver_name)
    

def simple_print_record():
    '''prints a simple unformated list of records for testing'''
    for i in speeding_records:
        print(i)

def print_all_record():
    '''prints a formated list of all records'''
    print(" ")
    #prints the header for the records
    #outside of for loop to prevent printing multiple times
    print_header()
    #for loop to run through all the records
    for i in speeding_records:
        #stores driver info in varible to avoid f string error
        driver = i["driver"]
        licence = i["licence"]
        limit = i["limit"]
        speed = i["speed"]
        # prints all records
        print_record(driver,licence,limit,speed)


def display_summary():
    '''prints a sumamry of all total offences, total fines, average over speed limit, and highest offence.'''
    print("-------------------------------")
    #creates a few varibles
    total_offences = len(speeding_records)
    total_fines = 0
    highest_offence_person = False
    highest_offence_speed = 0
    over_speed = []
    for i in speeding_records:
        #stores speed and limit, and overspeed in varibles for easier use
        limit = i["limit"]
        speed = i["speed"]
        over_limit = speed-limit

        #adding up fines
        fine = cal_speed_fine(speed,limit)
        total_fines += fine

        #add speed to list
        over_speed.append(over_limit)

        #checks if offender is highest offence and sets them as the new if they are
        if over_limit > highest_offence_speed:
            #sets the new highest speeder
            highest_offence_person = i["driver"]
            highest_offence_speed = over_limit

    # collecting varibles for printing the patrol summary
    avg_speed = statistics.mean(over_speed) #gets avg of speed
    #prints summary
    print("PATROL SUMMARY")
    print("")
    print(f"Total offences:            {total_offences}")
    print(f"Total fines issued:        ${total_fines}")
    print(f"Avgerage over speed limit: {avg_speed:.1f} km/h")
    print(f"Highest offence:           {highest_offence_person} ({highest_offence_speed} km/h over) ")
    print("-------------------------------")
        

def find_record_number(type,record):
    '''gets a record based on the type and returns the order on the list that the record is in'''
    #loops through speeding records to a record
    #if they find it
    list_of_same_records = []
    for i in speeding_records:
        if i[type] == record:
           list_of_same_records.append(i)
    return list_of_same_records


def print_searched_records(list_records):
    '''prints all the searched records for search records function'''
    #prints the results if found if not found if it isn't found 
    if len(list_records) == 0:
        print("record not found")
    else:
        print_header()
        for i in list_records:
            driver = i["driver"]
            licence = i["licence"]
            limit = i["limit"]
            speed = i["speed"]
            print_record(driver,licence,limit,speed)

def search_records():
    '''search records for a name or licence and prints it out'''
    print("-------------------------------")
    searhing = True #varibles to check user is still searching
    #while loop to get user to input valid data
    while searhing:
        #asks the user what data they want to search for
        print("What option do you want")
        print("1 : licence search")
        print("2 : Full name search")
        #collects the input
        type_of_search = input("Your option: ")
        
        if type_of_search == "1": #searching for licence
            #gets the licence
            record_input = input("Input their licence: ")
            #forces the user to input a correct licence if it's wrong
            while not licence_valid(record_input):
               record_input = input("Input their licence correctly: ") 
            #formats the record to be in full uppercase before trying to find it
            record_input = record_input.upper()
            record_numb = find_record_number("licence",record_input)

            #prints the results if found if not found if it isn't found 
            print_searched_records(record_numb)
            searhing = False

        elif type_of_search == "2": #searching for full name
            #gets the full name
            record_input = input("Input their full name: ")
            find_record_number("driver",record_input)
            #formats the record into title case before trying to find it
            record_input = record_input.title()
            record_numb = find_record_number("driver",record_input)
            
            #prints the results if found if not found if it isn't found 
            print_searched_records(record_numb)
            searhing = False

        else: 
            #handles invalid options
            print("invalid option input 1 or 2 ")


#
def password_check(password):
    '''checks if password is correct'''

    #hashes the password inpute
    hashed_userpass = hashlib.sha256(password.encode('utf-8')) 
    #converts the hash into human readable characters 
    text_hahsed_userpass = hashed_userpass.hexdigest()

    if text_hahsed_userpass == database_password:
        return True
    else:
        return False




#-----------------------------------------------
#-----------------------------------------------
# main loop
#-----------------------------------------------
#-----------------------------------------------

#only allows the user pass if they get the password
print("-------------------------------")
while incorrect_password:
    #user input password
    
    print("")
    user_input_pass = input("Input database password: ")
    print("")
    #
    if password_check(user_input_pass):
        incorrect_password = False
        print("Password is correct")
        print("letting you in")
    else:
        print("Password is incorrect")
    print("")
    
print("-------------------------------")
        
# main program after password
while using_program:
    #prints the main menu of options
    print(" ")
    print("-------------------------------")
    print(" ")
    print("Main menu:")
    print("1: create a new record")
    print("2: view all records")
    print("3: search offence records")
    print("4: display patrol summary")
    print("5: Exit program")
    print(" ")
    #gets the user input
    user_input = input("Option picked: ")
    # go to the user input and output invalid input if invalid
    if user_input == "1":
        create_record()
    elif user_input == "2":
        print_all_record()
    elif user_input == "3":
        search_records()
    elif user_input == "4":
        display_summary()
    elif user_input == "5":
        using_program = False
        print(" ")
        print("*********")
        print("Good bye")
        print("*********")
    else:
        print(" ")
        print("invalid input")
    


#testing for loop storage
#for i in range(-100,100): print(f"{i}:{cal_speed_fine(i,0)}")
#for i in range(0,120): print(f"{i}{speed_valid(i)}")