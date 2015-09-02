import sys
sys.path.append('../src/util')
from primes import nextPrime,isPrime
from bloom import BloomFilter

def testNextPrime():
    n = nextPrime(1)
    assert n == 2
    n = nextPrime(70)
    assert n == 71

def testIsPrime():
    assert (isPrime(71))
    assert (not isPrime(1000000))

def testBloom():
    Filter = BloomFilter(1000000,0.000001)
    for i in range(1,1000000):
        if i%2 == 0 :
            Filter.insert(i)
    for i in range(1,1000000):
        if i%2 == 0:
            assert Filter.check(i)
        else :
            assert not Filter.check(i)
    Filter.clean()
    for i in range(1,1000000):
        if i%2 != 0 :
            Filter.insert(i)
    for i in range(1,1000000):
        if i%2 == 0:
            assert not Filter.check(i)
        else :
            assert Filter.check(i)

if __name__ == '__main__':
    testBloom()
    testIsPrime()
    testNextPrime()
