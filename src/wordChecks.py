
class wordChecks:
    checksBool = False

    def checkRack(self, word, rack):
        if word == None or word == " ":
            raise ValueError("Must input word")
        for char in word:
            if char in rack:
                checksBool = True
        return checksBool

    def checkInDict(self, word):
        dictionary = open("dic.txt").read()
        if word not in dictionary:
            checksBool = False
        else:
            checksBool = True
        return checksBool