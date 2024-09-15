from random import *
play=True
while play:
    a=input('Would you like to play hangman ?(yes/no):').lower()
    if a!='y' and a!='yes':
        print('See you later!')
        break
    words_ls=['shoes','cabbage','tank','copper','current',
              'month','van','crack','baseball','camera',
              'flower','jam','taste','price','train',
              'straw','theory','fork','motion','rule',
              'toad','stitch','limit','play','lake',
              'pancake','tail','bulb','mother','stew',
              'mint','yak','boot','grain','shape',
              'sheep','week','lunchroom','giants','change',
              'battle','crow','shade','sugar','number',
              'mask','son','society','sun','digestio']
    word=words_ls[randint(0,49)]
    w_guessed=['_']*len(word)
    guesses_wr=0
    print('You currently have 0 incorrect guesses.\nHere is your puzzles:')
    print(' '.join(w_guessed))
    for i in range(10):
        j=input('Please enter your guess:')
        for i in range(len(word)):
            if word[i]==j:w_guessed[i]=j
        if '_' not in w_guessed:
            print("Congratulations, you guessed a letter in the puzzle!")
            print('Your word is {}'.format(word))
            break
        elif j in word:
            print('\nCongratulations,you guessed a letter in the puzzle\n')
            print(' '.join(w_guessed))
        else:
            guesses_wr+=1
            print("Sorry,that letter is NOT in the puzzle.")
            print('You currently have {} incorrect guesses'.format(guesses_wr))
    else:
        print("you have run out of turns to guess")
    play=(False,True)[input('Do you want to play again?').lower() in ['y','yes']]