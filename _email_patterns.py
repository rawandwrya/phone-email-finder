#! /usr/bin/python3

'''
this module is an internal module that defines the email pattern that our program can find
'''
#__________________________________________________________________________________________
import re
#__________________________________________________________________________________________
__all__ = ['email_patterns']
#__________________________________________________________________________________________
_pattern1 = r'''(
	[a-z0-9.%_+-]+		# username
	@					# at
	[a-z0-9.-]{2,15}	# pre-DOT domain name
	\.[a-z]{2,5}		# DOT domain-host
	)
'''
#__________________________________________________________________________________________
def email_patterns():
	patterns = (
		_pattern1
	)
	return patterns
