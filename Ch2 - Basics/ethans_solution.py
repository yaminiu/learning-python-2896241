show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    temp=teststr.lower()
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c
            
    if newstr == newstr[::-1]:
        return True
    else:
        return "Owies!"
    # reversestr = ""
    # strindx = len(newstr)-1
    # while (strindx >=0):
    #     reversestr += newstr[strindx]
    #     strindx -= 1
    # if newstr == reversestr:
    #     return True
    # return False

for test in ["Radar", "Ethan ahte", "text"]:
    print(test, "is palindrome:", is_palindrome(test))