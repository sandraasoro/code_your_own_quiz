# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 14:41:50 2016

@author: OTeniola-LPTP
"""
# -*- coding: utf-8 -*-
#Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
def chooseDifficulty():
    print "Welcome!!!"
    print "Dare To Choose!!"
    print "To proceed, select a level by typing in Easy, Medium or Hard!"
    difficulty = raw_input("").lower()
    return difficulty
    
def EasyLevel():
#User selected "easy" difficulty level
#Returns question beginning with question 1 and ends at question 4. 
#Upon user answering all questions correctly, entire question will be printed out with all blanks filled in.
    question = "Making my way ___1___ walking fast. " \
    "Faces pass and I'm home ___2___. " "Staring blankly ___3___ just making my way. " \
    "Making a way through the ___4___." 
    UserInput = ["", "", "", ""]
    answers = ['downtown', 'bound', 'ahead', 'crowd']
    returnAnswers(question, UserInput, answers)
    print "Making my way downtown walking fast. Faces pass and I'm home bound. Staring blankly ahead just making my way. Making a way through the crowd." 
    print "Good job! Easy Level Completed!"
    input('Press ENTER to exit game')

def MediumLevel():
#User selected "medium" difficulty level
#Returns question beginning with question 1 and ends at question 4. 
#Upon user answering all questions correctly, entire question will be printed out with all blanks filled in.
    question = "If I could ___1___ into the sky. " "Do you think ___2___ would pass me by. " \
    "Because you know I'd walk a ___3___ miles. " \
    "If I could just see you ___4___."
    UserInput = ["", "", "", ""]
    answers = ["fall", "time", "thousand", "tonight"]
    returnAnswers(question, UserInput, answers)
    print "If I could fall into the sky. Do you think time would pass me by. Because you know I'd walk a thousand miles. If I could just see you tonight."
    print "Good job! Medium Level Completed!"
    input('Press ENTER to exit game')

def HardLevel():
#User selected "hard" difficulty level
#Returns question beginning with question 1 and ends at question 4. 
#Upon user answering all questions correctly, entire question will be printed out with all blanks filled in.
    question = "It is ___1___ times like this when I think of you. " "And I wonder if you ever ___2___ of me. " \
               "Because ___3___ is so wrong and I dont belong. " \
               "Living in your ___4___ memories."
    UserInput = ["", "", "", ""]
    answers = ["always", "think", "everything", "precious"]
    returnAnswers(question, UserInput, answers)
    print " It is always times like this when I think of you. And I wonder if you ever think of me. Because everything is so wrong and I dont belong. Living in your precious memories."
    print "Good job! Hard Level Completed!"
    input('Press ENTER to exit game')

def returnAnswers(question, UserInput, answers):
#Allows user to input a level and returns associated questions and answers pertaining to selected level.
#Returns questions and solutions for level user selected. 
    blanks = ['___1___', '___2___', '___3___', '___4___']
    blank = 0
    print question, "\n"
    question = question.split(". ")
    for line in question:
        print line
        while UserInput[blank].lower() != answers[blank]:
            UserInput[blank] = raw_input("Fill In The Blank: ")
            if UserInput[blank].lower() != answers[blank]:
                print "Please try again!"
        print "That is correct!"
        print line.replace(blanks[blank], answers[blank]), "\n"
        blank += 1

def MadLibsGame(difficulty):
#User selects difficulty level based off of only 3 choices (easy,medium,hard)
#If invalid level is choosen, game returns prompt to select a valid level
    if difficulty == "easy":
        EasyLevel()
    elif difficulty == "medium":
        MediumLevel()
    elif difficulty == "hard":
        HardLevel()
    else:
        print "Invalid level selected. Please select a valid level"
    return chooseDifficulty()  

# Begin the MadLibs Game!
MadLibsGame(chooseDifficulty())
