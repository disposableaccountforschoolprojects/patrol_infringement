import string
import statistics
licence_char = "aannnnnn" #characters of the licence a = letter n = numbers
licence_correct_length = len(licence_char) #gets length of licence_char to find the length licence plate should be 
speed_brackets = [30,110] #range of valid speed limts
using_program = True

speed_fines = { #specifies the fines you get for each speeding limit
    30:[1,10],
    80:[11,20],
    170:[21,30],
    400:[31,40],
    620:[41,999999999999],

}

speeding_records = [
    {"driver": "John Smith", "licence":"AB123456","limit":50,"speed":68 }
]

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
    

def print_record(driver,licence,limit,speed):
    '''gets data and prints out a single record'''
    #calcuates varibles like over limit and fine to reduce amount of parameters 
    over_limit = speed-limit
    fine = cal_speed_fine(speed,limit)
    #prints the record
    print(f"driver name:                {driver}")
    print(f"driver licence:             {licence}")
    print(f"posted speed limit:         {limit}")
    print(f"driver speed :              {speed}")
    print(f"Speed over the speed limit: {over_limit}")
    print(f"Fine:                      ${fine}")


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
                    print(f"Character {i+1} must be a alphabet ")
                    return False
            elif licence_char[i] == "n":
                if not licence[i].isdigit():
                    print(f"Character {i+1} must be a number ")
                    return False
        print("Pass checks licence has been added")
        return True
    else:
        print(f"licence must be {licence_correct_length} characters long")
        return False


def speed_valid(speed):
    '''checks if speed is a valid range and returns true or false'''
    if speed in range(speed_brackets[0],speed_brackets[1]+1):
        print("speed success added")
        return True
    else:
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
        driver_licence = input("Please input driver name correctly: ")

    print("")
    #Gets the speed_limit
    try:
        speed_limit = int(input(f"Input speed limit {speed_brackets[0]} and {speed_brackets[1]}: "))
    except: 
        print("Only input numbers")
    # if name isn't valid asks the user to input the name correctly until they do
    while not speed_valid(speed_limit):
        
        try:
            speed_limit = int(input("Input speed limit correctly: "))
        except: 
            print("Only input numbers")

    print("")
    driver_speed = 0
    # checks if the driver is above the speed limit and rejects the request if it isn't
    while driver_speed < speed_limit:
        try:
            driver_speed = int(input("Input driver speed: "))
            if driver_speed <= speed_limit:
                print("no speeding offence has occured in this speed input a correct speed")
        except: 
            print("Only input numbers")

    driver_name = driver_name.strip().title() # formats the driver name to be in title case and removes excess spaces.
    add_to_record(driver_name,driver_licence,speed_limit,driver_speed)
    print("")
    print_record(driver_name,driver_licence,speed_limit,driver_speed)
    warrent_check(driver_name)
    print("-------------------------------")
    

def simple_print_record():
    '''prints a simple unformated list of records for testing'''
    for i in speeding_records:
        print(i)

def print_all_record():
    '''prints a formated list of all records'''
    print("-------------------------------")
    #for loop to run through all the records
    for i in speeding_records:
        #stores driver info in varible to avoid f string error
        driver = i["driver"]
        licence = i["licence"]
        limit = i["limit"]
        speed = i["speed"]
        # prints all records
        print_record(driver,licence,limit,speed)
        print("-------------------------------")


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

    print(over_speed)
    # collecting varibles for printing the patrol summary
    avg_speed = statistics.mean(over_speed)
    #prints summary
    print("PATROL SUMMARY")
    print("")
    print(f"Total offences:            {total_offences}")
    print(f"Total fines issued:        ${total_fines}")
    print(f"Avgerage over speed limit: {avg_speed:.1f} km/h")
    print(f"Highest offence:           {highest_offence_person} ({highest_offence_speed} km/h over) ")
    print("-------------------------------")
        


# main loop
while using_program:
    print("Main menu:")
    print("1: create a new record")
    print("2: view all records")
    print("3: search offence records")
    print("4: display patrol summary")
    print("5: Exit program")
    user_input = input("Option picked: ")
    if user_input == "1":
        create_record()
    elif user_input == "2":
        print_all_record()
    elif user_input == "3":
        pass
    elif user_input == "4":
        display_summary()
    elif user_input == "5":
        using_program = False
        print("*********")
        print("Good bye")
        print("*********")
    else:
        print("invalid input")
    


#testing for loop storage
#for i in range(-100,100): print(f"{i}:{cal_speed_fine(i,0)}")
#for i in range(0,120): print(f"{i}{speed_valid(i)}")