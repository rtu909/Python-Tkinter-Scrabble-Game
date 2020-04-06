## @file wordChecks.py
#  @author The Trifecta
#  @brief This method implements conditional checks for a valid word.
#  @date Apr.06,2020

## @brief Checks if a word can be made from a rack.
#  @param1 the inputted word to check if its letters are in the rack.
#  @param2 the rack from which to check words letters.
#  @returns boolean indicating whether word can be made from rack.
#  @exceptions ValueError if empty string is entered
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

## @brief Checks if a word belongs in the scrabble dictionary.
#  @param1 the inputted word to check if it exists in the text file dictionary.
#  @returns boolean indicating word exists in the dictionary.
#  @exceptions IOError if text file cannot be found.
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
