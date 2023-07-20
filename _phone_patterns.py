#! /usr/bin/python3

import re

'''
This is an internal file that dictates what phone-number patterns can our program look for.


if you wish to add a new pattern, introduce it as a new raw string variable and add it (concatenate) to the pattern variable within the pattern function

Pattern specifications:
The patterns must have the following grouping-parentheses formats
( (?<=(<preceding country/company codes and formats>)) <phone number in different formats>)

A different pattern format will most likely cause errors.

'''
#______________________________________________________________________________________________________________________________
__all__ = ['phone_patterns']
#______________________________________________________________________________________________________________________________
# 7** *** **** formats of Iraqi phone numbers
# [**IMPORTANT: this must be the first variable in the pattern and the first line of pattern should not start with | **]
_ten_digit_local_iraqi_format = r'''
	((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\d{7})
	
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\s\d{7})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\s\d{3}\s\d{4})
	
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))-\d{3}-\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\s\d{3}-\d{4})
	
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\d{7})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\s\d{7})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\d{3}\s\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\s\d{3}\s\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\d{3}-\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\d{3}\s-\s\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\s\d{3}\s-\s\d{4})
	|((?<=(\D77[0-5]|\D75[0-1]|\D78[0-5]|\D760|\D790))\)\s\d{3}-\d{4})
'''

# 07** *** **** formats of Iraqi phone numbers
_eleven_digit_local_iraqi_format = r'''
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\d{7})
	
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\s\d{7})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\s\d{3}\s\d{4})
	
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))-\d{3}-\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\s\d{3}-\d{4})
	
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\d{7})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\s\d{7})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\d{3}\s\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\s\d{3}\s\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\d{3}-\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\d{3}\s-\s\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\s\d{3}\s-\s\d{4})
	|((?<=(077[0-5]|075[0-1]|078[0-5]|0760|0790))\)\s\d{3}-\d{4})
'''

# +964 7** *** **** formats of Iraqi phone numbers
_thirteen_digit_international_iraqi_format = r'''
	|((?<=(\+96477[0-5]|\+96475[0-1]|\+96478[0-5]|\+964760|\+964790))\d{7})
	
	|((?<=(\+964\s77[0-5]|\+964\s75[0-1]|\+964\s78[0-5]|\+964\s760|\+964\s790))\d{7})
	|((?<=(\+964\s77[0-5]|\+964\s75[0-1]|\+964\s78[0-5]|\+964\s760|\+964\s790))\s\d{3}\s\d{4})
	
	|((?<=(\+964-77[0-5]|\+964-75[0-1]|\+964-78[0-5]|\+964-760|\+964-790))-\d{3}-\d{4})
	|((?<=(\+964\s-\s77[0-5]|\+964\s-\s75[0-1]|\+964\s-\s78[0-5]|\+964\s-\s760|\+964\s-\s790))\s-\s\d{3}\s-\s\d{4})
	|((?<=(\+964-77[0-5]|\+964-75[0-1]|\+964-78[0-5]|\+964-760|\+964-790))\d{7})
	|((?<=(\+964\s-\s77[0-5]|\+964\s-\s75[0-1]|\+964\s-\s78[0-5]|\+964\s-\s760|\+964\s-\s790))\d{7})
	
	|((?<=(\+964\)77[0-5]|\+964\)75[0-1]|\+964\)78[0-5]|\+964\)760|\+964\)790))\d{7})
	|((?<=(\+964\)\s77[0-5]|\+964\)\s75[0-1]|\+964\)\s78[0-5]|\+964\)\s760|\+964\)\s790))\d{7})
	|((?<=(\+964\)\s77[0-5]|\+964\)\s75[0-1]|\+964\)\s78[0-5]|\+964\)\s760|\+964\)\s790))\s\d{3}\s\d{4})
	
	|((?<=(\+964\)77[0-5]|\+964\)75[0-1]|\+964\)78[0-5]|\+964\)760|\+964\)790))-\d{3}-\d{4})
	|((?<=(\+964\)\s77[0-5]|\+964\)\s75[0-1]|\+964\)\s78[0-5]|\+964\)\s760|\+964\)\s790))-\d{3}-\d{4})
	|((?<=(\+964\)\s77[0-5]|\+964\)\s75[0-1]|\+964\)\s78[0-5]|\+964\)\s760|\+964\)\s790))\s-\s\d{3}\s-\s\d{4})
'''

# 00964 7** *** **** formats of Iraqi phone numbers
_fourteen_digit_international_iraqi_format = r'''
	|((?<=(0096477[0-5]|0096475[0-1]|0096478[0-5]|00964760|00964790))\d{7})
	
	|((?<=(00964\s77[0-5]|00964\s75[0-1]|00964\s78[0-5]|00964\s760|00964\s790))\d{7})
	|((?<=(00964\s77[0-5]|00964\s75[0-1]|00964\s78[0-5]|00964\s760|00964\s790))\s\d{3}\s\d{4})
	
	|((?<=(00964-77[0-5]|00964-75[0-1]|00964-78[0-5]|00964-760|00964-790))-\d{3}-\d{4})
	|((?<=(00964\s-\s77[0-5]|00964\s-\s75[0-1]|00964\s-\s78[0-5]|00964\s-\s760|00964\s-\s790))\s-\s\d{3}\s-\s\d{4})
	|((?<=(00964-77[0-5]|00964-75[0-1]|00964-78[0-5]|00964-760|00964-790))\d{7})
	|((?<=(00964\s-\s77[0-5]|00964\s-\s75[0-1]|00964\s-\s78[0-5]|00964\s-\s760|00964\s-\s790))\d{7})
	
	|((?<=(00964\)77[0-5]|00964\)75[0-1]|00964\)78[0-5]|00964\)760|00964\)790))\d{7})
	|((?<=(00964\)\s77[0-5]|00964\)\s75[0-1]|00964\)\s78[0-5]|00964\)\s760|00964\)\s790))\d{7})
	|((?<=(00964\)\s77[0-5]|00964\)\s75[0-1]|00964\)\s78[0-5]|00964\)\s760|00964\)\s790))\s\d{3}\s\d{4})
	
	|((?<=(00964\)77[0-5]|00964\)75[0-1]|00964\)78[0-5]|00964\)760|00964\)790))-\d{3}-\d{4})
	|((?<=(00964\)\s77[0-5]|00964\)\s75[0-1]|00964\)\s78[0-5]|00964\)\s760|00964\)\s790))-\d{3}-\d{4})
	|((?<=(00964\)\s77[0-5]|00964\)\s75[0-1]|00964\)\s78[0-5]|00964\)\s760|00964\)\s790))\s-\s\d{3}\s-\s\d{4})
'''
#_________________________________________________________________________________________________________________________________
def phone_patterns():
	patterns = (
		_ten_digit_local_iraqi_format +
		_eleven_digit_local_iraqi_format +
		_thirteen_digit_international_iraqi_format +
		_fourteen_digit_international_iraqi_format
	)
	return patterns













