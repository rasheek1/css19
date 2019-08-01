def CountToN(num):
    num= abs(num)
    for i in range(1,num+1):
        print i

    '''
    i = 1
    while i <= num:
        print i
        i += 1
    '''

n = raw_input ("Enter an interger:\n")
n = int (n)

CountToN(n)

def Factors(num):
    num = abs(num)
    l = []

    for i in range(1,num+1):
        if num % i ==0:
            l.append(i)

    return l

print Factors(n)