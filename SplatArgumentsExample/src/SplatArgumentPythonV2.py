'''
Created on Oct 30, 2013

@author: Tristan
Here is an example on how to use Splat arguments in Python v2.x. Splat arguments tell python that you are
unsure of how many arguments will be passed into a function, but it will most likely be more than one.
'''

"""To use splat arguments, type a '*' before the input parameters, in this case, 'actors'.
When you call on the parameters, you only need the name of the parameter that you declared,
not the '*' """

def favorite_actors(*actors):
    """Prints out your favorite actorS (plural!)"""
    print "Your favorite actors are:",  actors
    
    
favorite_actors("Michael Palin", "John Cleese", "Graham Chapman")
favorite_actors("Sidney Poitier", "Bill Cosby")