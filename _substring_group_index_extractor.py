#! /usr/bin/python3

'''
This function takes in a matched object from re.finditer(<pattern>,<string>)
Returns the group indices for that matched object's substring matchs.

so that the substrings of the matched object can easily be accessed with <matched_object>.group(<index>)

How to use:
1- import it into the desired code from <relative.or.absolute.directory.to.the.module> import group_index_extractor
2- pass an RE match object to it with <variable_name> = group_index_extractor(<match_object>)
3- the substring index within the tuple-list of the substring matches will be passed back
'''

import re

__all__ = ['group_index_extractor']

def group_index_extractor(match_object):							# the object that is matched comes in
	substring_matches = match_object.groups()						# We list the substring patterns that have matched with our object
	list_of_substring_indeces=[]									# an empty list where we append the indeces to
	for substring in substring_matches:								# check the matches within the tuple-list one by one
		if substring != None:										# we skip the pattern groups that did not match with the object  
			substring_index = substring_matches.index(substring)	# store the index of the pattern that matches the object
			list_of_substring_indeces.append(substring_index)		# append the list of the indeces
	return list_of_substring_indeces								# return the re-match-object's group()index of the of the substring that matched the object
