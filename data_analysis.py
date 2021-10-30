from typing import Text
import urllib.request
import string
import sys 
from unicodedata import category 
import collections

def make_request(url):
    ''' Generic function that makes a request to the given url and returns the response '''
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text

def remove_header(text):
    ''' Finds indexes of starting and ending strings and returns a sliced text removing the indexes found'''
    start_indicator = "*** START OF THIS PROJECT GUTENBERG EBOOK MARK TWAIN'S SPEECHES ***"
    end_indicator = "End of the Project Gutenberg EBook of Mark Twain's Speeches by Mark"
    # find the position of the starting string
    start_index = text.find(start_indicator)
    # find the postiion of the ending string
    end_index = text.find(end_indicator)
    # add on the length of the string to starting index so it chops the whole string rather than just the first character
    slice_start_index = start_index + len(start_indicator)
    # return sliced string
    return text[slice_start_index:end_index]


def clean_data(text):
    ''' removes all puncuation from strings and returns a new list of cleaned strings'''
    words_in_speech = list(text.split())
    string_list = []
    # borrowed from professor's code
    strippables = ''.join([chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")])
    for word in words_in_speech:
        # make all words lowercase
        word = word.lower()
        # remove strippable characters from the end and beginning of the string
        word = word.strip(strippables)
        # remove strippable characters from the middle of the string
        word = word.replace(strippables, '')
        table = str.maketrans(dict.fromkeys(string.punctuation))
        new_s = word.translate(table)       
        string_list.append(new_s)
    # print(string_list)
    return string_list




def word_frequency(string_list):
    d = dict()
    for line in string_list: 
        words = line.split(" ")
        for word in words: 
            if word in d: 
                d[word] = d[word]+ 1 
            else: 
                d[word] = 1 
    for key in list(d.keys()):
        print(key, ":", d[key])
    return d

    

def most_common(cleaned_data,stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []
    stopwords = set(open('stopwords.txt').read().split())
    print(stopwords)
    if stopwords == True:
        cleaned_data = [w for w in cleaned_data if w not in stopwords]
    for w, freq in cleaned_data.items():
        t.append((freq,w))
    t.sort()
    t.reverse()
    return t

        


def main():
    text = make_request('https://www.gutenberg.org/files/3188/3188-0.txt')
    removed_header_footer = remove_header(text)
    cleaned_data = clean_data(removed_header_footer)
    new_dict = word_frequency(cleaned_data)
    t = most_common(new_dict,stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
   

if __name__ == '__main__':
    main()
        



import pickle

# Save data to a file (will be part of your data fetching script)

# with open('speeches.pickle','w') as f:
#     pickle.dump(string_list,f)


# # Load data from a file (will be part of your data processing script)
# with open('speeches.pickle','r') as input_file:
#     reloaded_copy_of_texts = pickle.load(input_file)




