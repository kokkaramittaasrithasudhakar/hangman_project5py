#hangman project

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
# import hangman_words
# chosen_word = random.choice(hangman_words.word_list) or
from hangman_words import word_list

#todo1.1:Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-5.1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
# import hangman_words
# chosen_word = random.choice(hangman_words.word_list) or

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False							#initial ie while not false means true so code runs until all blanks are filled
#Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#TODO-5.3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO-2.1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#Create blanks
display = []								#display (empty list to be filled)
for _ in range(word_length):				#find & store len of chosen word in word_length eg:5 then range(word_length)==range(5)
    display += "_"							#display _ on each iteration equal to word_length(range)

while not end_of_game:						#it loops until this turns true refer below
    # todo1.2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    
    #TODO-5.4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")  
      
    #TODO-2.2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    #Hint: Remember that you can use the .index() method to check if a letter is in a

    #eg:if chosen_word=baboon      0 to 5 (6th) position in a list.
        
    #Check guessed letter
    for position in range(word_length):		#eg baboon and position:0 range(5)
        letter = chosen_word[position]		# letter =chosen_word[0] =b(according to index)
                                            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:					#if b(letter form chosen_word at index 0)==b(guess)
            display[position] = letter		#display[0]=b(letter) and again loop go on with index 1 until len(word_lenth)
    
    #TODO-4.2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
    #Check if user is wrong.
    if guess not in chosen_word:			#when the guess is not true lives reduce by 1
        #TODO-5.5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")  
        lives -= 1
        if lives == 0:						#when lives is 0 the game is over(when lives keep going reaches 0 then the game is over)
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:					#todo 3.1 when all the blanks are filled and their is no _(blanks) then end_of_game =true you win .if go to while loop while not true is false so game ends
        end_of_game = True
        print("You win.")
    
    #TODO-4.3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    #TODO-5.2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])					#stages is a list of stages where the updated lives is the index
