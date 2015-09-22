from math import log
import array
from primes import nextPrime
from random import randint, seed
from bitarray import bitarray

class BloomFilter:
    """docstring for BloomFilter
    n is upperbound on number of elements to be inserted in BloomFilter
    failureProb is upperbound on probability of false positives"""
    def __init__(self, n, failureProb = 1e-5):
        #total size of bit array
        self.n = n
        self.m = nextPrime((int)(-n * log(failureProb) / (log(2)**2)))
        self.filter = bitarray()
        self.filter.append(False)
        self.filter = self.m * self.filter
        self.k = (int)(self.m*(log(2))/self.n)
        seed()
        self.hashes = [(randint(0,self.m-1),randint(0,self.m-1)) for i in range(0,self.k)]

    '''Reinitialize the bloom filter with new hash functions'''
    def clean(self):
        del self.filter
        self.filter = bitarray()
        self.filter.append(False)
        self.filter = self.m * self.filter
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

    '''Returns True if given value has been already inserted False otherwise
    Also stores the hash in bloom filter on the fly'''
    def checkAndInsert(self,num):
        wasPresent = True
        for i in range(0,self.k):
            idx = (self.hashes[i][0]*num + self.hashes[i][1])%self.m
            if self.filter[idx] == False:
                wasPresent = False
                self.filter[idx] = True
        return wasPresent
