'''
Created on Oct 30, 2013

@author: Tristan
Here is an example on how to use Splat arguments in Python. One can also use the 'splat' operator to perform exponentiation.
'''
def powerRiser(base, exponent):
    #We use the splat command in the following form: base ** exponent
    print (base ** exponent)

powerRiser(2,3)
powerRiser(1,2)
powerRiser(16,4)