import string
licence_char = "aannnnnn" #characters of the licence a = letter n = numbers
licence_correct_length = len(licence_char) #gets length of licence_char to find the length licence plate should be 
speed_brackets = [30,110] #range of valid speed limts
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
using_program = True

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

    #Gets the driver name
    driver_name = input("Input driver name: ")
    # if name isn't valid asks the user to input the name correctly until they do
    while not valid_name(driver_name):
        driver_name = input("Please input driver name correctly: ")


    #Gets the driver licence 
    driver_licence = input("Input driver licence: ")
    # if licence isn't valid a
    # sks the user to input the licence correctly until they do
    while not licence_valid(driver_licence):
        driver_licence = input("Please input driver name correctly: ")


    #Gets the speed_limit
    
    try:
        speed_limit = int(input("Input speed limit: "))
    except: 
        print("Only input numbers")
    # if name isn't valid asks the user to input the name correctly until they do
    while not speed_valid(speed_limit):
        
        try:
            speed_limit = int(input("Input speed limit correctly: "))
        except: 
            print("Only input numbers")


    driver_speed = 0
    while driver_speed < speed_limit:
        try:
            driver_speed = int(input("Input driver speed: "))
            if driver_speed < speed_limit:
                print("no speeding offence has occured in this speed input a correct speed")
        except: 
            print("Only input numbers")


    add_to_record(driver_name,driver_licence,speed_limit,driver_speed)
    

def simple_print_record():
    '''prints a simple unformated list of records for testing'''
    for i in speeding_records:
        print(i)

# main loop

while using_program:
    create_record()
    simple_print_record()


#testing for loop storage
#for i in range(-100,100): print(f"{i}:{cal_speed_fine(i,0)}")
#for i in range(0,120): print(f"{i}{speed_valid(i)}")