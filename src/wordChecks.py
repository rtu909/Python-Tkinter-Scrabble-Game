def checkRack(word, rack):
    checksBool = False
    if word == None or word == " ":
        raise ValueError("Must input word")
    wordUp = word.upper()
    for char in wordUp:
        if char in rack:
            checksBool = True
    return checksBool

def checkInDict(word):
    dicfile = open('dic.txt', 'r')
    file1 = dicfile.read()
    file1 = file1.split("\n")
    word = word.upper()
    if word in file1:
        checksBool = True
    else:
        checksBool = False
    dicfile.close()
    return checksBool
