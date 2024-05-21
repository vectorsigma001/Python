"""
Regular expressions (regex) are powerful tools for matching patterns in text. 
Here are some examples of how to use regular expressions in Python using the re module.
"""

#============Importing the re Module===============
import re



#==================Matching a Simple String=============
pattern = r"hello"
text = "hello world"

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("No match found.")

#Match found!



#==================Matching Digits===============

pattern = r"\d+"  # One or more digits
text = "There are 123 apples"

match = re.search(pattern, text)
if match:
    print(f"Match found: {match.group()}")
else:
    print("No match found.")
  
# Match found: 123

#=================Email Validation===================
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
emails = ["user@example.com", "user.name@domain.co", "invalid-email"]

for email in emails:
    if re.match(pattern, email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")
"""
Valid email: user@example.com
Valid email: user.name@domain.co
Invalid email: invalid-email
"""


#================Phone Number Validation==============
pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_numbers = ["(123) 456-7890", "123-456-7890", "(123)456-7890"]

for number in phone_numbers:
    if re.match(pattern, number):
        print(f"Valid phone number: {number}")
    else:
        print(f"Invalid phone number: {number}")
"""
Valid phone number: (123) 456-7890
Invalid phone number: 123-456-7890
Invalid phone number: (123)456-7890
"""


#===============Finding All Matches================
pattern = r"\b\w{4}\b"  # Words with exactly 4 letters
text = "This is a test text with some four letter words like this and that."

matches = re.findall(pattern, text)
print(matches)
"""
['test', 'with', 'some', 'four', 'like', 'this', 'that']
"""



#==================Substitution================
pattern = r"apples"
replacement = "oranges"
text = "I like apples. Apples are tasty."

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)
Output:
#I like oranges. oranges are tasty.




#================Splitting Strings================
pattern = r"\s*,\s*"  # Split on comma with optional whitespace
text = "apple, banana ,  cherry, date"

fruits = re.split(pattern, text)
print(fruits)
"""
['apple', 'banana', 'cherry', 'date0
"""

#=============Capturing Groups=================
pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "My phone number is 123-456-7890."

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Area code: {match.group(1)}")
    print(f"First 3 digits: {match.group(2)}")
    print(f"Last 4 digits: {match.group(3)}")

"""
Full match: 123-456-7890
Area code: 123
First 3 digits: 456
Last 4 digits: 7890
"""


#==========Named Groups============
pattern = r"(?P<area>\d{3})-(?P<first>\d{3})-(?P<second>\d{4})"
text = "My phone number is 123-456-7890."

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group('area')}-{match.group('first')}-{match.group('second')}")

"""
Full match: 123-456-7890

"""


#===========Lookahead and Lookbehind==========
#===========Positive Lookahead=============
pattern = r"foo(?=\d)"
text = "foo1 foo2 foo bar"

matches = re.findall(pattern, text)
print(matches)
"""
['foo', 'foo']
"""


#===========Negative Lookahead===============
pattern = r"foo(?!\d)"
text = "foo1 foo2 foo bar"

matches = re.findall(pattern, text)
print(matches)

"""
['foo']
"""


#==============Positive Lookbehind==============
pattern = r"(?<=\d)foo"
text = "1foo 2foo foo bar"

matches = re.findall(pattern, text)
print(matches)

"""
['foo', 'foo']
"""


#==========Negative Lookbehind=================
pattern = r"(?<!\d)foo"
text = "1foo 2foo foo bar"

matches = re.findall(pattern, text)
print(matches)
"""
['foo']
"""

"""
These examples should give you a good understanding of how to use regular expressions in 
Python for various tasks such as matching, searching, substituting, and splitting strings.
"""






