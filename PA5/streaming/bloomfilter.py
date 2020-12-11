# Python 3 program to build Bloom Filter
# This code is a modified version of the code presented in:
# 'https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/'

import mmh3

class BloomFilter(object):

    '''
    Class for Bloom filter, using murmur3 hash function
    '''

    def __init__(self, items_count, filter_size, hash_count):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        filter_size : int
            Size of the bloom filter in bits
        hash_count  : int
            Number of hash functions used in bloom filter
        '''
        # Size of bit array to use
        self.size = filter_size

        # number of hash functions to use
        self.hash_count = hash_count 

        # Bit array of given size
        self.bit_array = [0] * self.size


    def add(self, item):
        '''
        Add an item in the filter
        '''
        for i in range(self.hash_count):

            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size

            # set the bit True in bit_array
            self.bit_array[digest] = 1

    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == 0:

                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True
