import urllib.request

url = 'https://www.gutenberg.org/files/59603/59603-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing

url = 'https://www.gutenberg.org/files/59603/59603-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing


# import pickle

# # Save data to a file (will be part of your data fetching script)

# with open('dickens_texts.pickle','w') as f:
#     pickle.dump(,f)


# # Load data from a file (will be part of your data processing script)
# with open('dickens_texts.pickle','r') as input_file:
#     reloaded_copy_of_texts = pickle.load(input_file)
