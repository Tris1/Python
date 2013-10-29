'''
Created on Oct 29, 2013

@author: Tristan
Simply translates user input into correct Pig Latin. Have fun
'''

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == ('a' or 'e' or 'i' or 'u' or 'o'):
        new_word = word + pyg
        print (new_word)
    else:
        new_word = word[1:] + first + pyg
        print (new_word)
else:
    print ('We cannot translate your input! Please try again.')