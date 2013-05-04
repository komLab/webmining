import operator
import matplotlib.pyplot as plt

filename = './ger1'

def get_text():
	fh 	= open( filename, 'r' )
	text 	= fh.read()
	fh.close()
	return text
	
def print_text():
	print( get_text() )
	
def get_words( text ):
	#normalize
	text = text.lower()
	text = text.translate(None, r'"!.,()[]:;*/?%&')
	#split in words
	word_list = text.split()
	return word_list
	
def get_hash( word_list ):
	wordcount_hash = {}
	#iterate over all words (may contain duplicates)
	for word in word_list:
		#A check if word was processed before - continue
		if word in wordcount_hash:
			continue
		#B add word and word's existance count in the list into the hash
		wordcount_hash[word] = word_list.count( word )
	return wordcount_hash
	
def get_hash_without_stoppwords( word_list, stoppword_list ):
	wordcount_hash = {}
	count = 0
	#iterate over all words (may contain duplicates)
	for word in word_list:
		#A check if word was processed before - continue
		if word in wordcount_hash:
			count = count + 1
			continue
		if word in stoppword_list:
			continue
		#B add word and word's existance count in the list into the hash
		wordcount_hash[word] = word_list.count( word )
		count = count + 1
	return (wordcount_hash, count)

def get_stoppwords():
	fh 	= open( './german', 'r' )
	words 	= set( line.strip() for line in fh )
	fh.close()
	return words
	
	
def aufgabe_2a():
	#print_text()
	my_words	= get_words( get_text() )
	my_hash		= get_hash( my_words )
	my_sorted	= sorted(my_hash.iteritems(), key=operator.itemgetter(1), reverse=True)
	total_wordcount	= len( my_words )
	word_appearance	= float()
	print total_wordcount
	fh = open('./%s_erg' % filename, 'w')
	for item in my_sorted:
  		#print("%s,%i" %(item[0], item[1]) )
  		word_appearance	= float( item[1]*100 ) / float( total_wordcount ) 
  		fh.write("%s,%i,%f\n" %(item[0], item[1], word_appearance ) )
	fh.close()
	#print( sorted(my_hash.iteritems(), key=operator.itemgetter(1), reverse=True))
	#print( get_hash( get_words( get_text() ) ) )	
	
def aufgabe_2b():
	#print_text()
	my_words	= get_words( get_text() )
	my_stoppwords	= get_stoppwords()
	(my_hash, total_wordcount) = get_hash_without_stoppwords( my_words, my_stoppwords )
	my_sorted	= sorted(my_hash.iteritems(), key=operator.itemgetter(1), reverse=True)

	word_appearance	= float()
	
	print total_wordcount
	fh = open('./%s_erg_withoutSW' % filename, 'w')
	for item in my_sorted:
  		#print("%s,%i" %(item[0], item[1]) )
  		word_appearance	= float( item[1]*100 ) / float( total_wordcount ) 
  		fh.write("%s,%i,%f\n" %(item[0], item[1], word_appearance ) )
	fh.close()
	#print( sorted(my_hash.iteritems(), key=operator.itemgetter(1), reverse=True))
	#print( get_hash( get_words( get_text() ) ) )

def aufgabe_3a():#Zipf's
	my_words	= get_words( get_text() )
	my_stoppwords	= get_stoppwords()
	(my_hash, total_wordcount) = get_hash_without_stoppwords( my_words, my_stoppwords )
	my_sorted	= sorted(my_hash.values(), reverse=True)
	
	my_hash2	= get_hash( my_words )
	my_sorted2	= sorted(my_hash2.values(), reverse=True)
	
	plt.plot(my_sorted)
	plt.plot(my_sorted2)
	plt.ylabel('Appearance')
	plt.xlabel('Rank')
	plt.title('Die Brueder Wright - Wordappearance')
	plt.yscale('log')
	plt.xscale('log')
	plt.legend(['no stoppwords', 'stoppwords'])
	plt.show()

if __name__ == '__main__':
	aufgabe_3a()
	
	
	
	
	
	
	
	
	
