def checkRack(word, rack):
    checksBool = False
    if word == None:
        raise ValueError("Must input word")
    if rack == None:
        raise ValueError("Must input rack")
    else:
        wordUp = word.upper()
        for char in wordUp:
            if char in rack:
                checksBool = True
        return checksBool

def checkInDict(word):
    try:
        dicfile = open('dic.txt', 'r')
        file1 = dicfile.read()
    except IOError:
        print ("Error: can\'t find file or read data")
    else:
        file1 = file1.split("\n")
        word = word.upper()
        if word in file1:
            checksBool = True
        else:
            checksBool = False
        dicfile.close()
        return checksBool
