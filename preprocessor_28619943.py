#######################################################################
#                                                                     #
# This file contains the "Preprocessor" class.                        #
#                                                                     #
# The class contains a list that stores the input text, "input_text"  #
# in the constructor.                                                 #
#                                                                     #
# "__str__" is overwritten to display the length of the "input_text"  #
#                                                                     #
# A "tokenise" function is implemented to break the "input_text" to   #
# tokens.                                                             #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "Preprocessor".                                                     #
#                                                                     #
# This file will be used in main_28619943.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: May 19, 2018                                          #
# Last Modified: May 19, 2018, 03:07 PM                               #
#                                                                     #
#######################################################################


class Preprocessor:

    # initiate the class by declaring a list instance variable
    def __init__(self):
        self.input_text = []

    # override print function to show the length of the text
    def __str__(self):
        return str(len(self.input_text))

    # takes an arg param and tokenize it
    # assign the tokens to the list declared above
    def tokenise(self, input_sequence):
        self.input_text = input_sequence.split()

    # return the tokenized text as a list
    def get_tokenised_list(self):
        return self.input_text
