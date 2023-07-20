#! /usr/bin/python3

'''
This program scans copied UNICODE texts for iraqi mobile phone numbers and email adresses

copy the text and run the email_phone_finder.py file from a terminal

the .py file dependencies that are imported must be within the same directory

Made by: Rawand Wrya Mahmood, July 19, 2023
'''



import re
import pyperclip

from _phone_patterns import phone_patterns
from _substring_group_index_extractor import group_index_extractor
from _email_patterns import email_patterns
#________________________________________________________________________________________

# compile the phone number objects in phone_objects
phone_patterns = phone_patterns()
phone_objects = re.compile(phone_patterns, re.VERBOSE)

# compile the email objects in email_objects
email_patterns = email_patterns()
email_objects  = re.compile(email_patterns, re.VERBOSE | re.IGNORECASE)

# store the copies text within text
text = str(pyperclip.paste())

# store the matched phones and emails in phone_matches and email_matches
phone_matches = phone_objects.finditer(text)
email_matches = email_objects.finditer(text)
#_________________________________________________________________________________________

# Phone number output
print("\nthe following phone numbers were found:\n")
for match in phone_matches:
	list_of_substring_indeces = group_index_extractor(match)
	index = list_of_substring_indeces[1]
	if match.group(index):
		print(match.group(index+1)+match.group(index))

# email adress output
print("\nthe following emails were found:\n")
for match in email_matches:
	print(match.group()+"\n")
