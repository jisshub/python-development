# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def changeCase(myWord):
    for eachLetter in myWord:
        if eachLetter == eachLetter.lower():
            print(eachLetter.upper())
        else:
            print(eachLetter.lower())


changeCase(myWord="PythoNisTa")

