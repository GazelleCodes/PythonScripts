#The search function takes in three parameters, the filename, and two strings to search for.

import re

text = 'The quick brown fox jumps over the lazy dog'
pattern = "sample"

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match found.")


#The match function checks for a match only at the beginning of the string. If the pattern is found at the start of the string, it returns a match object; otherwise, it returns None.

pattern = r'The' #match the word "The" at the beginning of the string
text = 'The quick brown fox jumps over the lazy dog'

match = re.match(pattern, text)
if match:
    print("The test string starts with 'The'.")
else:
    print("The test string does not start with 'The'.")

# The fullmatch function checks for a match against the entire string. If the pattern matches the entire string, it returns a match object; otherwise, it returns None.

pattern = r'\d{4}-\d{2}-\d{2}' #match the entire string in YYYY-MM-DD format
date_string= '2023-10-15'

match = re.fullmatch(pattern, date_string)
if match:
    print(f"The date string {date_string} matches the pattern.")
else:
    print(f"The date string {date_string} does not match the pattern.")


# The findall function returns a list of all non-overlapping matches of the pattern in the string. If no matches are found, it returns an empty list.

pattern = r'\d+' #match all sequences of digits
text = 'There are 3 cats, 5 dogs, and 2 birds.'

matches = re.findall(pattern, text)
print("Found matches:", matches)


#sub and subn functions are used to replace occurrences of a pattern in a string. The sub function returns the modified string, while the subn function returns a tuple containing the modified string and the number of substitutions made.

pattern = r'\b\w{4}\b' #matchs a word that is exactly four letters long
text = 'This is a test string with some four-letter words like test, word, and code.'

modified_text = re.sub(pattern, '****', text)
print("Modified text:", modified_text)

# The split function splits the string by the occurrences of the pattern and returns a list of substrings.

pattern = r'\s+' #match one or more whitespace characters
text = 'This is a test string with multiple spaces.'

substrings = re.split(pattern, text)
print("Substrings:", substrings)

#The escape function is used to escape special characters in a string, making them literal characters in the regular expression.

pattern = r'\b' #match a word boundary, but we want to treat it as a literal string in our search pattern
text = 'This is a test string with word boundaries.'

escaped_pattern = re.escape(pattern)
match = re.search(escaped_pattern, text)

if match:
    print(f'Found a word boundary in the text')
else:
    print(f'No word boundary found in the text')

# The compile function compiles a regular expression pattern into a regular expression object, which can be used for matching using its match(), search(), findall(), etc. methods.

pattern = r'\d+' #match one or more digits
text = 'There are 3 cats, 5 dogs, and 2 birds.'

regex = re.compile(pattern)
matches = regex.findall(text)
print("Found matches using compiled regex:", matches)


#match objects returned by search, match, and fullmatch functions have several methods that provide information about the match. Some of the commonly used methods include:

pattern = r'(\d{3})-(\d{3})-(\d{4})' #match a phone number in the format XXX-XXX-XXXX
text = 'My phone number is 123-456-7890.'

match = re.search(pattern, text)

if match:
    print(f'Matched phone number: {match.group()}') #returns the entire matched string
    print(f'Area code: {match.group(1)}') #returns the first captured group (area code)
    print(f'phone number without area code: {match.group(2)}') #returns the second and third captured groups (phone number without area code)
    print(f'starts position: {match.start()}') #returns the starting index of the match
    print(f'ends position: {match.end()}') #returns the ending index of the match
    print(f'span: {match.span()}') #returns a tuple containing the start and end positions of the match
