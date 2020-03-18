
class wordChecks:
    def checkRack(word, rack):
        checksBool = False
        if word == None or word == " ":
            raise ValueError("Must input word")
        wordUp = word.upper()
        print(wordUp + " rack")
        for char in wordUp:
            if char in rack:
                checksBool = True
        return checksBool

    def checkInDict(word):
        dictionary = open("dic.txt").read()
        wordUp = word.upper()
        print(wordUp + " dict")
        if wordUp not in dictionary:
            checksBool = False
        else:
            checksBool = True
        return checksBool