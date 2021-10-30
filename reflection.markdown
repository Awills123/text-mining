# Reflection 

## Project Overview

For my project I decided to use Project Gutenburg and analyze a set of speeched done by Mark Twain. The goal of looking at a variety of speeches specifically was to see the similarities in his diction and what he reffered to most. To do this I first had to plan out my thought process and what I would do if we did not have to code. I first had to clean the data since it had a table of contents and various sections which affected the analysis of the text. After that I used word frequency to create tuple pairs of each word and their frequency. After that I created a list of the 20 most frequent words found in the text. My hopes for this project were to learn more about the diction used back then and what words he used most to influence a crowd. I wanted to create a system that shows the 20 most common words found in all of his speeches to learn more about public speaking and getting a message across. 

## Implementation
 <!-- [~2-3 paragraphs] Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did. -->

The hardest part of this assignment was to start my process of analysis to be completely honest. When I thought about it logically, I knew I had to strip the data and make a new list of only the words while excluding punctuation marks and other characters. I began by creating a function that loads in the text and with this I could begin to clean my data. This set of data included a variety of speeches from Mark Twain so I wanted to only keep his wirting without the introduction and headers. To do this i created another function that removed the header and footer from the file and only left the text as is without any other unneccesary writing. This function contained the .find function and spliced the data atcertain points wwhich I defined in the function. After I created this function which basically gave me the raw text, I needed to use this output to continue to clean my data and get rid of punctuation and create a list of only the words. I struggled with this part and had to choose between various different ways to clean my data. At first I was trying to go manually and use .replace to replace each unneccessary character with a " " but this did not work well. To finally get this to work I used code from the professor and used the strippables definition we had conducted a few classes before. After I defined my strippables I still was getting a weird output so I reached out for help and did some research and learned about the .maketrans function which created a table of the replacable characters. I used this function to get replace those characters and then create a new string list that appended the cleaned words. 

With this cleaned data, I could now begin to conduct some analysis on the speeches and get creative with it. I wanted to orginally look at each speech individually but there are too many to be able to splice each one. With this in mind I pivoted my goal of the project and decided to use word frequency to analyze his most used words in all of his speeches. I created a function called word_frequency and created a dictionary of each word and how many times they appear in the text. I applied this function to the cleaned data I had previously which gave me a new dictionary that I could apply to my next functions. After I had this function done, it was much easier to continue with the analysis by using the output this function gave me. I continued by creating another function which would output the 20 most common words while excluding stopwords like "a, the, I, they, etc". I loaded the stopwords into a txt file and then created a new dictionary with the words in the text that were not stopwords. With this dictionary I could load it only the relevant words and their frequency. To print everything, at the main function at the bottom of my code I defined a new variable that used most_common function to analyze the dictionary I had created with the word_frequency function. I then told the code to print only 20 of the most common words along with their frequency. The last part of my implementation was creating a function called random_words that output a set of random words according to their frequency. To print this I used the random_word function and told it to analyze  the dictionary I had created previously that included the word_frequency function. 

## Results

My results for this assignment were exactly what I wanted them to be. I wanted the top 20 words that were found throughout his speeches to learn the diction that was used back then. The word_frequency function gave an output that was too large to really understand so thats why I wanted to narrow it down to only 20 words. The result from the common_words function gave me the result I was looking for and some of the top words were: 
    
    1. one      381
    2. mr       362
    3. said     296
    4. now      270
    5. will     264
    6. years    238
    7. man      232
    8. know     229
    9. can      218
    10. time     199
    
After looking at these words, I did not really see a difference in diction back then but I was able to get a gist of what his speeches entailed. The fact that now and years were some of the top words gives me the idea that he was very invested into what happened in the future. He wanted a say in what happened in the coming years and wanted to make action in their present time. Other words that stood out to me were 'mr' and 'man' becuase it looks as though he only spoke to a male dominated community. This shows the type of era that he was in and the male dominance that was in place for society. This mix of words gives me a sense of firmness and confidence in his speeches with words like 'will' and 'know' being shown frequently. 

Still, this list of words did not really show me the true diction that was used back then so I decided to print a list of random words proportional to their frequency. Some words that were outputted were 'phraseology', 'prayer' and 'mere' which truly s



4. Reflection [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?