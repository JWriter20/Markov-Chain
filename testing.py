import Markov_Chain

if __name__ == '__main__':
    dict = Markov_Chain.findWords()
    Markov_Chain.generate(dict, "newStory.txt", 1000)
