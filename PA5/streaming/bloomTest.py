from bloomfilter import BloomFilter
from random import shuffle

items_count = 20 #no of items to add
filter_size = 8 * items_count
hash_count = 6

bloomf = BloomFilter(items_count, filter_size, hash_count)
print("Size of bit array:{}".format(bloomf.size))
print("Number of hash functions:{}".format(bloomf.hash_count))

# words to be added
word_present = ['abound','abounds','abundance','abundant','accessable',
				'bloom','blossom','bolster','bonny','bonus','bonuses',
				'coherent','cohesive','colorful','comely','comfort',
				'gems','generosity','generous','generously','genial']

# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
			'racism','hurt','nuke','gloomy','facebook',
			'geeksforgeeks','twitter']

for item in word_present:
	bloomf.add(item)

shuffle(word_present)
shuffle(word_absent)

test_words = word_present[:10] + word_absent
shuffle(test_words)
for word in test_words:
	if bloomf.check(word):
		if word in word_absent:
			print("'{}' is a false positive!".format(word))
		else:
			print("'{}' is probably present!".format(word))
	else:
		print("'{}' is definitely not present!".format(word))

        
with open('tbloom.txt', 'w') as file:
    file.write(''.join(map(str, bloomf.bit_array)))