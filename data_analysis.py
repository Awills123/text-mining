import urllib.request

url = 'https://www.gutenberg.org/files/59603/59603-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) # for testing

url = 'https://www.gutenberg.org/files/59603/59603-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text1 = data.decode('utf-8')
# print(text1) # for testing

def word_frequency():
    d = dict()
    for line in text: 
        line = line.strip()
        words = line.split(" ")
        for word in words: 
            if word in d: 
                d[word] = d[word]+ 1 
            else: 
                d[word] = 1 
    for key in list(d.keys()):
        return key, ":", d[key]

print(word_frequency(text1))

import pickle

# Save data to a file (will be part of your data fetching script)

with open('dickens_texts.pickle','w') as f:
    pickle.dump(data.txt,f)


# Load data from a file (will be part of your data processing script)
with open('dickens_texts.pickle','r') as input_file:
    reloaded_copy_of_texts = pickle.load(input_file)
