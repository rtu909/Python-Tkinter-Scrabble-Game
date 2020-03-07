
class wordChecks:
    def checkRack(self, word, rack):
        checksBool = False
        if word == None or word == " ":
            raise ValueError("Must input word")
        for char in word:
            if char in rack:
                checksBool = True
        return checksBool

    def checkInDict(self, word):
        dictionary = open("dic.txt").read()
        if word.upper() not in dictionary:
            checksBool = False
        else:
            checksBool = True
        return checksBool