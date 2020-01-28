file = open("TextFile.txt", "r")
allWords = file.read().split(" ")
for i in range(len(allWords)):
    print(allWords[i])
