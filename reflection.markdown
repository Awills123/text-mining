# Reflection 

## Project Overview

For my project I decided to use Project Gutenburg and analyze a set of speeched done by Mark Twain. The goal of looking at a variety of speeches specifically was to see the similarities in his diction and what he reffered to most. To do this I first had to plan out my thought process and what I would do if we did not have to code. I first had to clean the data since it had a table of contents and various sections which affected the analysis of the text. After that I used word frequency to create tuple pairs of each word and their frequency. After that I created a list of the 20 most frequent words found in the text. My hopes for this project were to learn more about the diction used back then and what words he used most to influence a crowd. I wanted to create a system that shows the 20 most common words found in all of his speeches to learn more about public speaking and getting a message across. 

## Implementation
 <!-- [~2-3 paragraphs] Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did. -->

The hardest part was to start my process of analysis to be completely honest. When I thought about it logically, I knew I had to strip the data and make a new list of only the words while excluding punctuation marks and other characters. I began by creating a function that loads in the text and with this I could begin to clean my data. This set of data included a variety of speeches from Mark Twain so I wanted to only keep his wirting without the introduction and headers. To do this i created another function that removed the header and footer from the file and only left the text as is without any other unneccesary writing. After I created this function which basically 


3. Results [~2-3 paragraphs + figures/examples] Present what you accomplished:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.



4. Reflection [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?