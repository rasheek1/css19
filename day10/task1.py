#how to defien a function
'''You start by typing the keyword def follolwed by the name of the function and then 
parentheses with a list of parameters separated by commas. last yoy add a colon after the close 
parenthesis and indent the next line for the body of the function'''

def f(x):
    return 2 * x + 3

'''The above function is named f. it takes one parameter which should be a number.
The function returns twice the parameter plus 3'''

'''Once a function is defined, you can use if by calling it. To call a function, you
must use the function's name followed by paraentheses with the arguments of the function 
enclosed in them. arguments are literals, objects, expressions or return-value 
function calls that takes the definition. The arguments are associated with the 
parameter in the same position as 
'''

#function call with literal
print f(2) #return 7

#function call with an expression 
print f(3 + 4 * 6) # return 

#function call with a function call
print f(f(6)) #return 33

v = 89
#function call with a variable
print f(v) #return 181

#Task 1
def Greater(x,y):
    if x >=y: 
        return x
    else: 
        return y


x = float(raw_input("Enter first number:"))
y = float(raw_input("Enter second number:"))

print Greater(x,y)

#Task 2

def echo():
    x = raw_input('Enter a string:')
    return x + x
print echo()

#Task 3

def numbers(x,y,z):
    v = x * y * z + 3
    print v

numbers(2,3,4)

#List 
'''WHat is a List?'''
'''A list is an ordered collection of objects'''
'''You access the elements of a list with an index which is a integer between 
-n to n-1 where n is the length of the list. Negative indices access the list in 
reverse and nonnegative index i, its equivalent negative index is n - i where 
n is the length of the list.'''

#creating a list 
1=[] #[] are callsed subscript operators.
#The above is an empty list

k = list 
j = [1,2,3,4,5,6,7,8,9,10]

#List methods
print "The original lists"
print "l =", l
print "k =", k
print "j =", j

l.append('a')
k.append('t')
j.append(k)

print "\nThe list after an append"
print "l =", l
print "k =", k
print "j =", j

l.insert(0,'h')
k.insert(0,'a')
j.insert(5,12) 

print "\nThe list after an insert"
print "l =", l
print "k =", k
print "j =", j

print "\nThe list after an remove"
print "l =", l
print "k =", k
print "j =", j

l.pop()
k.pop()
j.pop()

print "\nThe list after an pop"
print "l =", l
print "k =", k
print "j =", j

l = [2,3,6,7,8]
k = [4,1,5,12,13]

print "\nThe index of 5 in each list"
print "l=", l.index(5)
print "k=", k.index(5)
print "j=", j.index(5)

#Loops
#while loops
#counting to 10 starting from 1
i = 1
while i <= 10:
    print i
    i += 1

#counting to 20 starting from 1
i = 1
while i <= 20:
    print i 
    i += 1

#counting to 20 starting from 1 but only odd numbers
i = 1
while i <= 20:
    if i % 2 == 1:
        print i 
    i += 1

v = ""
while v != "hello":
    v = raw_input("Enter a string:")

#for loop
#it is used for traversing sequences 

for i in range (1,11):
    print i

for i in range(1, 21):
    print i 

for i in range(2,21,2):
    print i 

for i in range(1,21):
    if i % 2 == 0:
        print i

for i in range(1,21):
    if i % 2 == 1:
        print i

for i in "This is a string":
    print i

h = []

for i in range(20):
    h.append(0)

print h, len(h)

h[1] = 1

for i in range(2,20):
    h[i] = h[i-1] + h[i-2]
        
print h

#dictionary
d = {}
b = dict()
a = {1:2,2:1,3:3,4:5,5:4}
c = {12:"John Smith",89:"Jane Doe"}

print a[1]

print c[89]

#Adding elements to a dictionary 

c[72] = "Joe Brown"

print c

#dictionary
'''What is an Object'''
'''An instance of a class'''

class person:
    def__init__(self,name):
    self.name = name
    self.age = 0

def birthday(self):
    self.age += 1
#Create objects
t = Person("Jane Doe") #Created a Person object

print t.name, t.age

s = Person("Roger Sam")

print s.name, s.age

t.birthday()

print t.name, t.age
