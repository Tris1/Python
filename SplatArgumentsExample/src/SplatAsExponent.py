'''
Created on Oct 30, 2013

@author: Tristan
Here is an example on how to use Splat arguments in Python. One can also use the 'splat' operator to perform exponentiation.
'''
#Check python version
import sys
python2 = False

if sys.version_info[:2] <= (3, 0):
    python2 = True
    
if python2 == True:
    print ("Please download SplatAsExponentV2.py to run this program on your system.")
    sys.exit(2)

def powerRiser(base, exponent):
    #We use the splat command in the following form: base ** exponent
    print (base ** exponent)

powerRiser(2,3)
powerRiser(1,2)
powerRiser(16,4)