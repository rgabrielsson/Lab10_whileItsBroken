import string

#get original list of words
def getWordList(file,length):
    words = []
    infile = open(file,"r")
    for line in infile:
        line = line.strip()
        words.append(line)
    while True:
        filtered_words = []
        for word in words:
            if len(word) == length:
                filtered_words.append(word)
        if len(filtered_words) == 0:
            print("That length is not permitted.")
            word_length = int(input("Enter a word length: "))
        else:
            return filtered_words

def list_to_string(list):
    newstr = ""
    for item in list:
        newstr = newstr+str(item)
    print(newstr)



#get locations of guessed letter in string
def getLocs(word,guess):
    locs = []
    for i in range(len(word)):
        if word[i] == guess:
            locs.append(i)
    display_string = ""
    for i in range(len(word)):
        if i in locs:
            display_string = display_string + guess
        else:
            display_string = display_string + "-"
    return display_string



def partition(word_list,guess):
    classDict = {}
    for word in word_list:
        display_string = getLocs(word,guess)
        if display_string in classDict:
            classDict[display_string] += word
        else:
            classDict[display_string] = list(word)
    return classDict
    

def largest_set(wordDict):
    maxKey = ""
    maxSet = []
    for key in wordDict:
        if len(wordDict[key]) > len(maxSet):
            maxKey = key
            maxSet = wordDict[key]
    return (maxKey,maxSet)
        



def main():
    #get word list and length
    word_length = int(input("Enter a word length: "))
    words = getWordList("ScrabbleWords.txt",word_length)  

    #setup for game
    bad_guesses = 0
    letters_guessed = []
    display = ["-"]*word_length
    list_to_string(display)

    #game
    win = False
    while not win and bad_guesses < 6:
        guess = input("Enter a single letter: ")
        guess = guess.lower()
        while len(guess) != 1 or not (guess in string.ascii_letters):
            print("Invalid guess")
            guess = input("Enter a single letter: ")
            guess = guess.lower()
        
        classDict = partition(words,guess)
        maxKey,maxSet = largest_set(classDict)
        words = maxSet
        for i in range(len(display)):
            if maxKey[i] != "-":
                display[i] = guess
        list_to_string(display)

        if "-" not in display:
            win == True
            print("You win!")
        else:
            bad_guesses += 1
        if bad_guesses >= 10:
            print("You lose!")
            print(f"The answer was {maxSet[0]}.")
    
main()
