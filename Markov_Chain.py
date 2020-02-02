import random

def findWords(file):
    dict = {}
    startWords = []
    file = open(file + ".txt", "r")
    allWords = file.read().split(" ")

    for i in range(len(allWords)-1):

        if allWords[i] in dict:
            if '.' in allWords[i]:
                if "." not in allWords[i+1]:
                    if "\"\n" not in allWords[i+1]:
                        startWords.append(allWords[i+1])
            dict.get(allWords[i]).append(allWords[i+1])
        else:
            dict[allWords[i]] = [allWords[i+1]]
    dict["StartWords"] = startWords
    return dict

def generate(dict, file, numWords):
    newFile = open(file + ".txt", "w+")
    output = ""
    count = 0
    currWord = random.choice(list(dict["StartWords"]))
    while count < int(numWords):
        if currWord not in dict.keys():
            currWord = random.choice(list(dict.keys()))
        if '.' in currWord:
            next = random.choice(list(dict["StartWords"]))
        else:
            next = random.choice(dict[currWord])
        output += (currWord + " ")
        currWord = next
        count += 1
    newFile.write(output)
    return



