#how to define a function
'''You start by typing the 
keyword def followed by the 
name of the function and then
parenthese with a list of
parameters seperated by commas.
last you add a colon after the 
close parenthesis and indent the next
line for the body of the function'''

def f():
    return 2 * x + 3

'''The above function is name f.
it tahe one paremeter which should
be a number.The function returnd
twice the paremeter plus 3'''

'''once a function is defined, you can use
it by calling it.to call a function, you must
use the function's name followed by parenthesis 
with the argument of the function enclosed in
them. argument are literals, objects, expressions
or return

#functon call with a lieral
print f(2)#return 7

#functon call with expression
print f(3+ 4 * 6) return 57

#function call with a function call
print f(f(6)) #return 33

v = 89
#function call with variable
print f(v)#return 181

