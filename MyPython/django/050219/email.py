import re

email4 = re.compile('[\w.]+')
match = email4.search('abc')
print(match.group())


