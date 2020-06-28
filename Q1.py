word=input('Enter a word\t')

all_freq = {} 
  
for letter in word: 
    if letter in all_freq: 
        all_freq[letter] += 1
    else: 
        all_freq[letter] = 1
print(str(all_freq))