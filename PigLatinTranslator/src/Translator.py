'''
Created on Oct 29, 2013

@author: Tristan
Simply translates user input into correct Pig Latin. Have fun
'''
#Check python version
import sys
python2 = False

if sys.version_info[:2] <= (3, 0):
    python2 = True
    
if python2 == True:
    print ("Please download TranslatorV2.py to run this program on your system.")
    sys.exit(2)

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