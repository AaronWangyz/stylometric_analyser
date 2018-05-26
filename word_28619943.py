#######################################################################
#                                                                     #
# This file contains the "WordAnalyser" class.                        #
#                                                                     #
# The class contains a pandas dataframe to store the character        #
# occurrence, "word_occ" in the constructor.                          #
#                                                                     #
# "__str__" is overwritten to display the structure of "word_occ".    #
#                                                                     #
# An "analyse_words" function is implemented to analyze the           #
# occurrence of each characters in the given file.                    #
#                                                                     #
# An "get_stopword_frequency" function is implemented to analyze the  #
# occurrence of stop words in the given file.                         #
#                                                                     #
# An "get_word_length_frequency" function is implemented to analyze   #
# the occurrence of each word length in the given file.               #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "WordAnalyser".                                                     #
#                                                                     #
# This file will be used in main_28619943.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: May 21, 2018                                          #
# Last Modified: May 25, 2018, 10:11 PM                               #
#                                                                     #
#######################################################################
import re
import pandas as pd
import numpy as np
import urllib.request


class WordAnalyser:

    # initialize the class by declaring a pandas dataframe called "word_occ",
    # with two columns, and one index
    def __init__(self):
        self.word_occ = pd.DataFrame(columns=["Word", "Word_Occurrence"])
        self.word_occ.set_index("Word")

    # re-write the str function to show the structure of "char_occ"
    def __str__(self):
        # initialize output variable with a header
        output = "\nWord occurrence: \n"

        # loop through "word_occ" and concatenate keys and values
        for i, row in self.word_occ.iterrows():
            output += "Word: " + row.Word + "\n" + "Word_Occurrence: " + str(row.Word_Occurrence) + "\n"

        return output

    # function to analyze the occurrence of words in a given file
    # this function takes an arg, "taokenised_list", which should be a tokenised
    # list process by "Preprocessor" class
    def analyse_words(self, tokenised_list):

        # define a regexp patters that only takes letters only
        punc_check = "^([A-Z]{1}|[a-z]{1})+$"

        # loop through "tokenised_list"
        # this loop gets the words
        for each in tokenised_list:

            # check if the "word" is actually a word
            if re.match(punc_check, each):

                # if it is a word, check if the word exists in the "word_occ" df
                if each in self.word_occ.Word.values:

                    # if it exits, find the index of that row
                    index = int(np.where(self.word_occ.Word == each)[0])

                    # then increment the occurrence of that row
                    self.word_occ.loc[index].Word_Occurrence += 1

                else:

                    # if it does not exist, add a new row and assign the occurrence as 1
                    self.word_occ = self.word_occ.append({"Word": each, "Word_Occurrence": 1}, ignore_index=True)

        # sort the df by "Word_Occurrence" column, in descending order
        self.word_occ = self.word_occ.sort_values(by=["Word_Occurrence"], ascending=False)

    # function to analyze the occurrence of stop words in the given text
    def get_stopword_frequency(self):

        # store the url of the website that contains the list of stop words
        url = "http://www.lextek.com/manuals/onix/stopwords1.html"

        # declare a local file that will store the raw html downloaded
        local_filename = "stop_words.txt"

        # retrieve the whole html code from the website
        urllib.request.urlretrieve(url, local_filename)

        # access the file that contains raw html just downloaded
        # and store the html in "text"
        f = open("stop_words.txt", "r")
        text = f.readlines()
        f.close()

        # reopen the file in "write" mode
        # overwrite the file so it contains stop words only
        # using the regexp declared
        f = open("stop_words.txt", "w")
        pattern = "^([A-Z]{1}|[a-z]{1})+$"
        for line in text:
            if re.match(pattern, line):
                f.write(line)
        f.close()

        # access the file again, store the stop words in a list
        with open("stop_words.txt", "r") as f:
            stop_words = f.readlines()
        f.close()

        # declare a new df to store the result of stop word analysis
        stop_word_occ = pd.DataFrame(columns=['Word', 'Word_Occurrence'])

        # loop through the "word_occ" df
        for each in self.word_occ.Word.values:

            # meanwhile loop through the "stop_words" list
            for stop_word in stop_words:

                # check if current element in "word_occ" is a stop word
                # adding "\n" because it cannot be striped
                if each+'\n' == stop_word:

                    # if current element is a stop word
                    # record its index
                    index = int(np.where(self.word_occ.Word == each)[0])

                    # then copy it to the "stop_words_occ" df
                    stop_word_occ = stop_word_occ.append(self.word_occ.loc[index], ignore_index=True)

        # rename columns in "stop_words_occ" df
        stop_word_occ = stop_word_occ.rename(columns={"Word": "Stop_Words"})
        stop_word_occ = stop_word_occ.rename(columns={"Word_Occurrence": "Stop_Word_Occurrence"})

        # sort the df by "Stop_Word_Occurrence" column, in descending order
        stop_word_occ = stop_word_occ.sort_values(by=["Stop_Word_Occurrence"], ascending=False)

        return stop_word_occ

    # function to analyze the occurrence of each word length in the given text
    def get_word_length_frequency(self):

        # declare a new df called "word_length_freq",
        # with two columns, and one index
        word_length_freq = pd.DataFrame(columns=['Length', 'Frequency'])
        word_length_freq.set_index("Length")

        # loop through "word_occ"
        for each in self.word_occ.Word.values:

            # check if the length of current word exists in "word_length_freq"
            if len(each) in word_length_freq.Length.values:

                # if it exists, find its index
                index = int(np.where(word_length_freq.Length == len(each))[0])

                # then increment the frequency by 1
                word_length_freq.loc[index].Frequency += 1

            else:

                # if it does not exist, add a new row and assign frequency as 1
                word_length_freq = word_length_freq.append({"Length": len(each), "Frequency": 1}, ignore_index=True)

        # sort the df by "Frequency" column, in descending order
        word_length_freq = word_length_freq.sort_values(by=["Frequency"], ascending=False)

        return word_length_freq
