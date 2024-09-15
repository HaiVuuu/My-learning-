import random
import time
import string

print('Welcome to Mastermind!!!\n')
print('At each turn, you will enter your guess for the playing board.')
print('A valid guess ahs 4 values in between 0 and 5.')
print('Each guess will have each number within the guess separated by a space.')
print('When you are ready, enter your first guess.')
print('From that point on, you will be told how many perfect and imperfect matches you have.')
print('After this message, you should guess again. You have 10 chances, good luck!\n')
answer=list(map(str,[random.randint(0,6) for i in range(4)]))
answer=(' '.join(answer))
chances=0
starttime=time.time()
end=time.time()
ex=end-starttime
for i in range(10):
    end=time.time()
    ex=end-starttime
    guest=input().split()
    pf_match=0
    impf_match=0
    chances+=1
    for i in range(4):
        if guest[i]==answer[i]:pf_match+=1
        elif guest[i] in answer:impf_match+=1
    print('You have {0} perfect matches and {1} imperfect matches'.format(pf_match, impf_match))
    if pf_match==4:
        print('Your have won the game in {} turn and {}!!!'.format(chances,time.strftime("%M:%S", time.gmtime(ex))))
        break
else:
    print('Sorry you have exceed the maximum numbers of turns. You lose. :((((')
    print('Here is the winning board',answer)