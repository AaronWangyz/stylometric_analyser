#######################################################################
#                                                                     #
# This file contains the "AnalysisVisualiser" class.                  #
#                                                                     #
# The class contains a pandas dataframe to store all the frequencies  #
# and occurrences analyzed, "frequency_chart" in the constructor.     #
#                                                                     #
# An "visualise_character_frequency" function is implemented to show  #
# a barchart of character analysis result.                            #
# This result does not contain punctuations.                          #
#                                                                     #
# An "visualise_punctuation_frequency" function is implemented to     #
# show a barchart of punctuation analysis result.                     #
#                                                                     #
# An "visualise_stopword_frequency" function is implemented to show a #
# barchart of stop word analysis result.                              #
#                                                                     #
# An "visualise_word_length_frequency" function is implemented to     #
# show a barchart of word length analysis result.                     #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "AnalysisVisualiser".                                               #
#                                                                     #
# This file will be used in main_28619943.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: May 25, 2018                                          #
# Last Modified: May 26, 2018, 02:27 PM                               #
#                                                                     #
#######################################################################
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


class AnalysisVisualiser:

    # initialize the class by taking an arg input "all_text_stats"
    # which is expected to be the result of all analyses
    # then declare a pandas dataframe called "frequency_chart"
    # to store the arg passed

    # !!!!!!!!!!!!!!!!! Important !!!!!!!!!!!!!!!!!#
    # In my implementation, "all_text_stats" is    #
    # defined as a "datafram of dataframes."       #
    # With the structure of:                       #
    # Type      Dataframe                          #
    #                                              #
    ################################################
    def __init__(self, all_text_stats):
        self.frequency_chart = all_text_stats

    # function top plot the character analysis result
    def visualise_character_frequency(self):

        # declare a new df to store the result of character occurrence analysis
        char_occ = pd.DataFrame(columns=["Character", "Char_Occurrence"])

        # get the index of "Char_Frequency"
        # which is the row contains character analysis result df
        char_df_index = int(np.where(self.frequency_chart.Type == "Char_Frequency")[0])

        # define regexp that only takes letters
        pattern = "^[a-zA-Z]|[0-9]$"

        # loop through the character df to remove punctuations
        # > ".loc[char_df_index" goes to the row that contains character analysis result df
        # > ".Dataframe" access the column named "Dataframe" in this row
        # > ".Character" access the column named "Character" in the dataframe accessed last step
        # > ".values" returns a list of values in the "Character" column
        for each in self.frequency_chart.loc[char_df_index].Dataframe.Character.values:

            # check if the current element is a letter
            if re.match(pattern, each):

                # if it is, find it index
                index = int(np.where(self.frequency_chart.loc[char_df_index].Dataframe.Character == each)[0])

                # then copy it to "char_occ" df
                char_occ = char_occ.append(self.frequency_chart.iloc[char_df_index].Dataframe.iloc[index], ignore_index=True)

        # sort the df by "Char_Occurrence" column, in descending order
        char_occ = char_occ.sort_values(by=["Char_Occurrence"], ascending=False)

        # plot a barchart and show it
        plt.bar(char_occ.iloc[:, 0].values, char_occ.iloc[:, 1].values, color="blue")
        plt.show()

    # function top plot the punctuation analysis result
    # exact same process as "visualise_character_frequency" because both them are part of the character analysis
    # only differents are:
    # 1. for this one, we find elements that does not match the regexp
    # 2. rename the columns appropriately
    def visualise_punctuation_frequency(self):

        punc_occ = pd.DataFrame(columns=["Character", "Char_Occurrence"])

        char_df_index = int(np.where(self.frequency_chart.Type == "Char_Frequency")[0])

        pattern = "^[a-zA-Z]|[0-9]$"

        for each in self.frequency_chart.loc[char_df_index].Dataframe.Character.values:
            if not re.match(pattern, each):
                index = int(np.where(self.frequency_chart.loc[char_df_index].Dataframe.Character == each)[0])
                punc_occ = punc_occ.append(self.frequency_chart.iloc[char_df_index].Dataframe.iloc[index], ignore_index=True)

        punc_occ = punc_occ.sort_values(by=["Char_Occurrence"], ascending=False)
        punc_occ = punc_occ.rename(columns={"Character": "Punctuation"})
        punc_occ = punc_occ.rename(columns={"Char_Occurrence": "Punc_Occurrence"})

        plt.bar(punc_occ.iloc[:, 0].values, punc_occ.iloc[:, 1].values, color="blue")
        plt.show()

    # function top plot the stop word analysis result
    def visualise_stopword_frequency(self):

        # find the index of the row contains stop word analysis df
        stop_word_df_index = int(np.where(self.frequency_chart.Type == "Stopword_Frequency")[0])

        # copy the whole df
        stop_word_occ = self.frequency_chart.loc[stop_word_df_index].Dataframe

        # then plot
        plt.bar(stop_word_occ.iloc[:, 0].values, stop_word_occ.iloc[:, 1].values, color="blue")
        plt.show()

    # exact same process as "visualise_stopword_frequency"
    # just changed a name
    def visualise_word_length_frequency(self):
        word_length_df_index = int(np.where(self.frequency_chart.Type == "Word_Length_Frequency")[0])
        word_length_occ = self.frequency_chart.loc[word_length_df_index].Dataframe

        plt.bar(word_length_occ.iloc[:, 0].values, word_length_occ.iloc[:, 1].values, color="blue")
        plt.show()
