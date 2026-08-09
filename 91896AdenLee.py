import string
LICENCE_LENGTH = 8 #what the licence length should be
licence_char = "aannnnnn" #characters of the licence a = letter n = numbers
speed_brackets = [30,110] #range of valid speed limts
speed_fines = {
    30:[1,10],
    80:[11,20],
    170:[21,30],
    400:[31,40],
    620:[41,999999999999],

}

def licence_valid(licence):
    '''Checks if the licence is valid'''
    licence_length = len(licence) # gets length of licence
    
    #checks if licence is correct length
    if licence_length == LICENCE_LENGTH:
        #loops through all char in licence
        for i in range(0,LICENCE_LENGTH):
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
        #invalid licence
        print("Invalid licence length")
        print(f"Licence must be {LICENCE_LENGTH}")
        return False


def speed_valid(speed):
    '''checks if speed is a valid range and returns true or false'''
    if speed in range(speed_brackets[0],speed_brackets[1]+1):
        return True
    else:
        return False

def cal_speed_fine(speed,speed_limit):
    speed_over = speed-speed_limit
    for i in speed_fines:
        if speed_over in range(speed_fines[i][0],speed_fines[i][1]+1):
            return i


while True:
    licence_valid(input())

#for i in range(-100,100): print(f"{i}:{cal_speed_fine(i,0)}")
#for i in range(0,1000): print(f"{i}{speed_valid(i)}")