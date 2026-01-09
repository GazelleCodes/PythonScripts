import re

with open('info.txt', 'r') as data:
  contents = data.read()

result = re.search(r'\d+\s\w+\s\w+\s\w+\s\#\d+\s\w+\s\w+\,\s\w+\s\d+\s\w+', contents)

print(result.group())
