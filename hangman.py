#hangman game
import random
#importing a random list of words 
from wordsFile import word_list
def game(word):
    tries=3
    guessed=False 
    guessed_letters=[]
    guessed_word=[]
    word_completion='_'*len(word)
    print(word_completion)
    while  not guessed and tries > 0:
        guess=input('Guess a letter or a word :').upper()
        #checks if guess   is single letter  and is a alphabet
        if len(guess)==1 or len(guess)<len(word) and guess.isalpha():
            #checks if word is already guessed
            if guess in guessed_letters:
                print('Letter is already guessed :',guess)
            #checks if guess is right and appends letter to guessed letters
            elif guess not in word:
                print('Guessed letter is wrong ')
                tries=tries-1
                guessed_letters.append(guess)
            #checks if guess is right and appends letter to guessed letters
            else:
                print("letter guessed is correct ")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                #places the guessed letter in proper position in the word
                indice=[i for i, letter in enumerate(word) if letter == guess]
                for index in indice:
                    word_as_list[index]=guess
                word_completion=''.join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
         #checks if guess is a word  and is a alphabet
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_word:
                print('Already guessed the following word :',guess)
            elif guess!= word:
                print('guessed word is wrong :')
                guessed_word.append(guess)
                tries-=1
            else:
                print('Guessed word is correct :')
                guessed=True
                word_completion=word
        #if i guess is anything else
        else:
            print('Not a valid guess : ')
            print("retry guess")
        print(word_completion)
    if guessed:
        print('you have made a correct guess and won the game')
    else:
        print('you have run out of tries. The word is ',word )


def main():
    word =random.choice(word_list).upper()
    print('Lets play hangman')
    game(word)
    play=input('Do you want to continue: Y/N').upper()
    if play=='Y':
       game(word)
        
        

if __name__ == "__main__":
    main()

                    
                
                
                
                
                
            
            
    