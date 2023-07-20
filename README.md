# phone-email-finder
A python program that will scan a copied text from the clipboard and returns potential Iraqi phone numbers and email addresses from the copied text.

# Instructions
Copy the desired text to scan
Run email_phone_finder.py from a terminal

# Documentations

## Dependencies
The program needs to import "re" and "pyperclip" python built-in modules
The program needs to import from 3 internal modules that need to be included within the program directory
  the 3 internal modules are email_patterns.py, phone_patterns.py,  and substring_group_index_extractor.py
  ### email_patterns.py
  email patterns that are required for re email compiled objects are defined here
  ### phone_patterns.py
  phone number patterns that are required for re phone number compiled objects are defined here
  ### substring_group_index_extractor.py
  returns the group() index of each matched substring pattern

## Running the Program
when running email_phone_finder.py from a terminal:
  ### imports all the necessary modules
  ### compiles the necessary re objects
  ### stores the the copied text from the clipboard
  ### scans the text for the compiled object matches
  ### returns the matches, if any, on the terminal

## Limitations
the programs is subject to re module limitations such as scanning only UNICODE characters.




