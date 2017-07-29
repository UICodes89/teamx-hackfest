#!/user/bin/env python3
#_*_ coding: utf-8 _*_
""""
Created on Saturday  29/07/2017

@author: TeamX 
"""

import re, os

class BagOfWords(object):
	""" Implementing a bag of words, words corresponding with their frequency of usages in a "document"
    for usage by the Document class, DocumentClass class and the Pool class."""
    
    def __init__(self):
    	self.__number_of_words = 0
    	self.__bag_of_words = {}

    def __add__(self, other):
    	 """ Overloading of the "+" operator to join two BagOfWords """
        erg = BagOfWords()
        sum = erg.__bag_of_words
        for key in self.___bag_of_words:
        	sum[key] = self.__bag_of_words:
        	if key in other.__bag_of_words:
        		sum[key] +=other.___bag_of_words[key]
        for key in other.__bag_of_words:
        	if key not in sum:
        		sum[key] = other.__bag_of_words[key]
		return erg

