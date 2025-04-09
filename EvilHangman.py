import string
import random

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

#convert list to string
def list_to_string(list):
    newstr = ""
    for item in list:
        newstr = newstr+str(item)
    return newstr

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


#break word_list into dictionary based on where the guessed letter is
def partition(word_list,guess):
    classDict = {}
    for word in word_list:
        display_string = getLocs(word,guess)
        if display_string in classDict:
            (classDict[display_string]).append(word)
        else:
            lst_word = [word]
            classDict[display_string] = lst_word
    return classDict
    
#find the largest set of words in the guess pattern dictionary and return that set
def largest_set(wordDict):
    maxKey = ""
    maxSet = []
    for key in wordDict:
        if len(wordDict[key]) > len(maxSet):
            maxKey = key
            maxSet = wordDict[key]

        #in the event of a tie, return the set the reveals the fewest letters
        elif len(wordDict[key]) == len(maxSet):
            if key.count("-") >= maxKey.count("-"):
                maxKey = key
                maxSet = wordDict[key]
    return (maxKey,maxSet)
        

#main game
def evilHangman():
    #get word list and length
    word_length = input("Enter a word length: ")
    test = True
    try:
        int(word_length)
    except ValueError:
        print("Since you decided not to enter a number, we will select 5.")
        word_length = "5"
    word_length = int(word_length)

    words = getWordList("ScrabbleWords.txt",word_length)  

    #setup for game
    bad_guess_threshold = 10
    bad_guesses = 0
    letters_guessed = []
    display = ["-"]*word_length
    saved_display = list_to_string(display)

    #game
    while bad_guesses < bad_guess_threshold:
        print(list_to_string(display))
        guess = input("Enter a single letter: ")
        guess = guess.lower()
        while len(guess) != 1 or not (guess in string.ascii_letters):
            print("Invalid guess")
            guess = input("Enter a single letter: ")
            guess = guess.lower()
        letters_guessed.append(guess)
        
        classDict = partition(words,guess)
        maxKey,maxSet = largest_set(classDict)
        words = maxSet
        for i in range(len(display)):
            if maxKey[i] != "-":
                display[i] = guess
        list_to_string(display)

        if "-" not in display:
            break
        elif saved_display == list_to_string(display):
            bad_guesses += 1
            print("Bad Guess")
            print(f"You have {bad_guess_threshold-bad_guesses} guesses remaining.")
            print(f"You have already guessed: {letters_guessed}")
        else:
            saved_display = list_to_string(display)
            print("Good Guess")
            print(f"You have {bad_guess_threshold-bad_guesses} guesses remaining.")
            print(f"You have already guessed: {letters_guessed}")
    
    if bad_guesses >= bad_guess_threshold:
        print("You lose!")
        print(f"The answer was {random.choice(maxSet)}.")
    else:
        print("Congratulations! You win!")
        print(f"{bad_guesses} bad guesses were needed to guess the word")
        
    
evilHangman()
