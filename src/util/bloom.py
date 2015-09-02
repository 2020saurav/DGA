from math import log
from primes import nextPrime
from random import randint,seed

class BloomFilter:
    """docstring for BloomFilter
    n is upperbound on number of elements to be inserted in BloomFilter
    failureProb is upperbound on probability of false positives"""
    def __init__(self, n, failureProb = 1e-5):
        #total size of bit array
        self.n = n
        self.m = nextPrime((int)(-n * log(failureProb) / (log(2)**2)))
        self.filter = [False]*self.m
        self.k = (int)(self.m*(log(2))/self.n)
        seed()
        self.hashes = [(randint(0,self.m-1),randint(0,self.m-1)) for i in range(0,self.k)]

    '''Reinitialize the bloom filter with new hash functions'''
    def clean(self):
        del self.filter
        self.filter = [False]*self.m
        del self.hashes
        seed()
        self.hashes = [(randint(0,self.m-1),randint(0,self.m-1)) for i in range(0,self.k)]

    '''Insert a given number in the bloom filter'''
    '''insert and check functions can be merged for better performance'''
    def insert(self,num):
        #Can be parallelized
        for i in range(0,self.k):
            self.filter[(self.hashes[i][0]*num + self.hashes[i][1])%self.m]=True

    '''Returns Ture if given value has been already inserted'''
    def check(self,num):
        for i in range(0,self.k):
            if self.filter[(self.hashes[i][0]*num + self.hashes[i][1])%self.m] == False:
                return False
        return True
