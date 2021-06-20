#
# usage: 
#   user@computer$ python exercise.py file1.txt file2.txt file3.txt

import sys

sys.argv 

# all of the arguments passed into the program by the operating system when it runs
# for example: python exercise.py file1.txt file2.txt file3.txt 
# sys.argv looks like this: ['exercise.py', 'file1.txt', 'file2.txt', 'file3.txt']


#test_files = [file1, file2, file3]
test_files = sys.argv[1:]
  
for test_file in test_files:
  try:
    tried_file = open(test_file, 'r')
  
  except FileNotFoundError:
    print(tried_file, "does not exist!")
  
  except:
    print(tried_file, "cannot be opened!")

  counts = dict() # {} is an alternative  
  words = tried_file.read().split() # return to this to filter out junk like '\n'

  total_words = len(words)

  for word in words:
    counts[word] = counts.get(word, 0) + 1
  
  least_freq_count = min(list(counts.values()))
  max_freq_count = max(list(counts.values()))
  
  least_freq_words = []
  most_freq_words = []

  for word, count in counts.items():
    if count == least_freq_count:
      least_freq_words.append(word)
    if count == max_freq_count:
      most_freq_words.append(word)
  
  print("most frequent words: {}".format(most_freq_words))
  print("least frequent words: {}".format(least_freq_words))
  print("total words: {}".format(total_words))
    # get the new minimum
    # get the new maximum

'''   
    frequent_word = None
    infrequent_word = None
    bigword = dict()
    smallword = dict()

  # we have a complete counts object

  for word, count in counts.items():
    if frequent_word is None or count >= frequent_word:
      bigword[frequent_word] = frequent_word.get(word)

    if infrequent_word is None or count <= infrequent_word:
      smallword[infrequent_word] = infrequent_word.get(word)

  print(“filename: “, tried_file)
  print(“total words: “, total_words)
  print(“most frequent words: “, bigword)
  print(“least frequent words: “, smallword)
'''

