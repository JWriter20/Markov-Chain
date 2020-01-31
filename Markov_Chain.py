import random

def findWords():
    dict = {}
    startWords = []
    file = open("TextFile.txt", "r")
    allWords = file.read().split(" ")
    for i in range(len(allWords)-1):
        if allWords[i] in dict:
            if '.' in allWords[i]:
                startWords.append(allWords[i+1])
            dict.get(allWords[i]).append(allWords[i+1])
        else:
            dict[allWords[i]] = [allWords[i+1]]
    dict["StartWords"] = startWords
    return dict

def generate(dict, file, numWords):
    newFile = open(file, "w+")
    output = ""
    count = 0
    currWord = random.choice(list(dict["StartWords"]))
    while count < numWords:
        if currWord not in dict.keys():
            currWord = random.choice(list(dict.keys()))
        if '.' in currWord:
            next = random.choice(list(dict["StartWords"]))
        next = random.choice(dict[currWord])
        output += (currWord + " ")
        currWord = next
        count += 1
    newFile.write(output)
    return



