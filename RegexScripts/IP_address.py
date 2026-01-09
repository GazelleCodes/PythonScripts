import re

# IP Addresses

with open('info.txt', 'r') as data:
  contents = data.read()

result = re.search(r'\d+\.\d+\.\d+\.\d+', contents)

print(result.group())
