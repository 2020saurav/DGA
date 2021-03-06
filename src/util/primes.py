from random import randint

''' Returns a prime greater than n '''
def nextPrime(n):
    assert n > 0
    n += 1
    while isPrime(n) != True:
        n += 1
    return n

''' Returns True if n is prime False otherwise'''
def isPrime(n):
    if n == 2 :
        return True
    if n % 2 == 0 :
        return False
    i = 3
    while i*i <= n :
        if n % i == 0 :
            return False
        i += 2
    return True

''' Get large random prime '''
def getLargeRandomPrime():
    largeNumber = randint(10**9, 10**10)
    return nextPrime(largeNumber)
