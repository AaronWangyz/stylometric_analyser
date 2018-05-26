#######################################################################
#                                                                     #
# This file contains the "CharacterAnalyser" class.                   #
#                                                                     #
# The class contains a pandas dataframe to store the character        #
# occurrence, "char_occ" in the constructor.                          #
#                                                                     #
# "__str__" is overwritten to display the structure of "char_occ".    #
#                                                                     #
# An "analyze_characters" function is implemented to analyze the      #
# occurrence of each characters in the given file, this includes      #
# letters, numbers, and punctuations.                                 #
#                                                                     #
# An "get_punctuation_frequency" function is implemented to analyze   #
# the occurrence of punctuations in the given file.                   #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "CharacterAnalyser".                                                #
#                                                                     #
# This file will be used in main_28619943.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: May 21, 2018                                          #
# Last Modified: May 21, 2018, 04:50 PM                               #
#                                                                     #
#######################################################################
import re
import pandas as pd
import numpy as np


class CharacterAnalyser:

    # initialize the class by declaring a pandas dataframe called "char_occ",
    # with two columns, and one index
    def __init__(self):
        self.char_occ = pd.DataFrame(columns=['Character', 'Char_Occurrence'])
        self.char_occ.set_index('Character')

    # re-write the str function to show the structure of "char_occ"
    def __str__(self):

        # initialize output variable with a header
        output = "\nCharacter occurrence: \n"

        # loop through "char_occ" and concatenate keys and values
        for i, row in self.char_occ.iterrows():
            output += "Character: " + row.Character + "\n" + "Char_Occurrence: " + str(row.Char_Occurrence) + "\n"

        return output

    # function to analyze the occurrence of characters in a given file
    # this function takes an arg, "taokenised_list", which should be a tokenised
    # list process by "Preprocessor" class
    def analyze_characters(self, tokenised_list):

        # loop through "tokenised_list"
        # this loop gets the words
        for each in tokenised_list:

            # then loop through each letter in the word
            for letter in each:

                # check if the letter is in the "char_occ" df
                if letter in self.char_occ.Character.values:

                    # if letter exists, find the index of that row
                    index = int(np.where(self.char_occ.Character == letter)[0])

                    # then increment the occurrence of the row found by the index
                    self.char_occ.loc[index].Char_Occurrence += 1

                else:

                    # if letter does not exist, create a new row and assign 1 to the occurrence
                    self.char_occ = self.char_occ.append({"Character": letter, "Char_Occurrence": 1}, ignore_index=True)

        # sort the df by "Char_Occurrence" column, in descending order
        self.char_occ = self.char_occ.sort_values(by=["Char_Occurrence"], ascending=False)

    # function to analyze the occurrence of punctuations in the given file
    def get_punctuation_frequency(self):

        # declare a new df to store the result of punctuation analysis
        punc_occ = pd.DataFrame(columns=['Character', 'Char_Occurrence'])

        # define a regexp patters that only takes letters or numbers
        # "A" only or "a" only or "1" only
        punc_check = "^([A-Z]{1}|[a-z]{1}|[0-9]{1}){1}$"

        # loop through the values of "Character" column
        for each in self.char_occ.Character.values:

            # for each elements in the "Character" column
            # find any element that does not match the regexp patter
            # (find non-letter and non-number elements, which are punctuations)
            if not re.match(punc_check, each):

                # record the index of the found punctuation
                index = int(np.where(self.char_occ.Character == each)[0])

                # copy the row from "char_occ" to "punc_occ"
                punc_occ = punc_occ.append(self.char_occ.loc[index], ignore_index=True)

        # rename the "punc_occ" df
        punc_occ = punc_occ.rename(columns={"Character": "Punctuation"})
        punc_occ = punc_occ.rename(columns={"Char_Occurrence": "Punc_Frequency"})

        # sort the df by "Punc_Frequency" column, in descending order
        punc_occ = punc_occ.sort_values(by=["Punc_Frequency"], ascending=False)

        return punc_occ
