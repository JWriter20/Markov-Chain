import random
import re
"""
Author: Jake Writer
Project description: This program provides the methods to be used when creating a Markov Chain. FindWords will create a
dictionary of word keys and values using the inputted file and generate will use that dictionary, and create a 
new text doc containing a story which uses the words from the initial file. This new file will have the inputted 
number of words
Date: 2/3/2020
"""

"""
Name of Method: findWords 
Argument types: String file
purpose: To create a dictionary with key value pairs from the inputted file
Assumptions: File that is taken in exists and is in the same folder
"""
def findWords(file):
    dict = {}
    startWords = []
    file = open(file + ".txt", "r")
    allWords = file.read().replace("\n", " ").split()

    for i in range(len(allWords)-1):
        if allWords[i] in dict.keys():
            if '.' in allWords[i]:
                if "." not in allWords[i+1]:
                    if "\"\n" not in allWords[i+1]:
                        startWords.append(allWords[i+1])
            dict.get(allWords[i]).append(allWords[i+1])
        else:
            dict[allWords[i]] = [allWords[i+1]]
    dict["StartWords"] = startWords
    return dict


"""
Name of Method: Generate 
Argument types: Dictionary dict, String file (will automatically add the .txt), int numWords
purpose: To create a new story using the dictionary and output it to a new doc.
Assumptions: dict exists and numWords is greater than or equal to 0, if you write to an existing file
it will override it
"""
def generate(dict, file, numWords):
    newFile = open(file + ".txt", "w+")
    output = ""
    count = 0
    currWord = random.choice(list(dict["StartWords"]))
    while count < int(numWords):
        willOutput = False
        willOutput2 = False
        if (count+1) % 20 == 0:
            willOutput2 = True
        if currWord not in dict.keys():
            currWord = random.choice(list(dict.keys()))
        if '.' in currWord:
            next = random.choice(list(dict["StartWords"]))
            randNum = random.randint(0, 4)
            if randNum is 1:
                willOutput = True
        else:
            next = random.choice(dict[currWord])
        output += (currWord + " ")
        currWord = next
        if willOutput2:
            output += "\n"
        if willOutput:
            output += "\n\n"
        count += 1
    newFile.write(output)
    return



