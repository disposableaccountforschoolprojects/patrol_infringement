import string
LICENCE_LENGTH = 8 #what the licence length should be
licence_char = "aannnnnn" #characters of the licence a = letter n = numbers

def licence_valid(licence):
    licence_length = len(licence)
    
    if licence_length == LICENCE_LENGTH:
        for i in range(0,LICENCE_LENGTH):
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
        print("Invalid licence licence length")
        print(f"Licence must be {LICENCE_LENGTH}")
        return False


while True:
    licence_valid(input())