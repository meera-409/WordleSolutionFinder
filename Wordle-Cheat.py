import csv
import sys


def main():


    #Read in possible answers from text file and store in list
    wordle_answers = []
    with open("wordle-answers-alphabetical.txt", "r") as wordle_txtfile:
        wordle_answers=wordle_txtfile.readlines()

    wordle_answers = [i.rstrip('\n') for i in wordle_answers] #remove "\n" from strings



    word_len=len(wordle_answers)


    #Continue asking for guesses until there is only 1 possible solution
    while word_len>1:


        
        guess = input("enter guess: ") #ask for guess user gave to wordle
        green = input("enter position of any green letters (separated by a common if needed): ") #ask for position index of the green letters (1-5)


        #if all letters are green, set wordle_answers to guess and end while loop
        if green.replace(" ", "") == "1,2,3,4,5":
            word_len=1
            wordle_answers = [guess]
            break


        #initialise lists and sets from index of green, yellow and grey letters
        grey = {1,2,3,4,5}
        list_green = []
        list_yellow = []


        yellow = input("enter position of any yellow letters (separated by a common if needed): ") #ask for position index of the yellow letters (1-5)

        #initialise array of words to remove from possible answers
        to_remove = []
        
        #if there are green letters in the guess
        if len(green.replace(" ", ""))>0:       #remove any spaces from string
            list_green = green.split(",")       #split string into indexes
            list_green = [int(i) for i in list_green]       #turn string to int
            grey = grey - set(list_green)   #remove the green letters from the grey set


            #for each possible wordle answer, add to the remove array if the letters don't match the green letters
            for word in wordle_answers:
                for i in list_green: #check each letter that was green in guess
                    if guess[i-1] != word[i-1]:
                        to_remove.append(word)
                        break   #break loop to not repeat word for rest of letters in green list
       
        

            to_remove = list(set(to_remove))    #remove duplicates if they occur
            for removee in to_remove:
                wordle_answers.remove(removee)  #remove each word that is not a possible answer from answer list

        #initialise array of words to remove from possible answers
        to_remove = []

        
        #if there are yellow letters in the guess
        if len(yellow.replace(" ", "")) > 0:      #remove any spaces from string  
            list_yellow = yellow.split(",")     #split string into indexes
            list_yellow = [int(i) for i in list_yellow] #turn string to int
            grey = grey - set(list_yellow)      #remove the yellow letters from the grey set

            #for each possible wordle answer, add to the remove array if the letters aren't in the word or letter is in the yellow spot
            for word in wordle_answers:
                for i in list_yellow:
                    if guess[i-1] not in word or guess[i-1]==word[i-1]:
                        to_remove.append(word)
                        break   #break loop to not repeat word for rest of letters in green list


            to_remove = list(set(to_remove))    #remove duplicates if they occur
            for removee in to_remove:
                wordle_answers.remove(removee)  #remove each word that is not a possible answer from answer list

        #initialise array of words to remove from possible answers
        to_remove = []
        

        grey = list(grey)   #convert to list

    
        if len(grey)> 0:
            for word in wordle_answers:
                for i in grey:
                    if guess.count(guess[i-1]) == 1:
                        if guess[i-1] in word:
                            to_remove.append(word)
                            break
                    else:
                        lst = []
                        for pos,char in enumerate(guess):
                            if(char == guess[i-1]):
                                lst.append(pos+1)
                        
                        single_char_grey = list(set(lst)-set(list_green)-set(list_yellow))
                        for pos in single_char_grey:
                            if guess[pos-1] == word[pos-1]:
                                to_remove.append(word)
                                break
                        else:
                            continue  # only executed if the inner loop did NOT break
                        break  # only executed if the inner loop DID break


            for removee in to_remove:
                wordle_answers.remove(removee)  #remove each word that is not a possible answer from answer list
        
        #check number of possible answers
        word_len=len(wordle_answers)

        #print list of possible answers if there's more than one
        if word_len > 1:
            print(wordle_answers)



    #if there is no possible words remaining
    if word_len == 0:
        sys.exit("No word found")

    #prints the only possible solution
    if word_len == 1:
        print("The answer is", wordle_answers[0])
        

    

