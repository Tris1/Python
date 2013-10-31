'''
Created on Oct 30, 2013

@author: Tristan
Here is an example on how to use Splat arguments in Python. Splat arguments tell python that you are
unsure of how many arguments will be passed into a function, but it will most likely be more than one.
'''

#Check python version
import sys
python2 = False

if sys.version_info[:2] <= (3, 0):
    python2 = True
    
if python2 == True:
    print ("Please download SplatArgumentV2.py to run this program on your system.")
    sys.exit(2)

"""To use splat arguments, type a '*' before the input parameters, in this case, 'actors'.
When you call on the parameters, you only need the name of the parameter that you declared,
not the '*' """

def favorite_actors(*actors):
    """Prints out your favorite actorS (plural!)"""
    print ("Your favorite actors are:",  actors)
    
    
favorite_actors("Michael Palin", "John Cleese", "Graham Chapman")
favorite_actors("Sidney Poitier", "Bill Cosby")