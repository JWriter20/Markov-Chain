import Markov_Chain
"""
Author: Jake Writer
Project description: This is the main file that takes in the inputs and uses the methods from Markov_Chain to 
create a new doc and output the new story to it.
Date: 2/3/2020
"""
if __name__ == '__main__':
    trainingFile = input("Please enter the name of the file you want to train the algorithm on: ")
    numWords = input("Please enter the number of words you want your new story to be: ")
    fileName = input("please input the name of the file on which you want to create your story: ")
    dict = Markov_Chain.findWords(trainingFile)
    Markov_Chain.generate(dict, fileName, numWords)

