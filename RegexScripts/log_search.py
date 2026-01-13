result = []

def search(filename, text):
    with open(filename) as f:
        for line in f:
            if text in line and 'nobody' in line:
                print(line)
                result.append(line)

search('secure.log', 'Failed')
