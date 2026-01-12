result = []

def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text in line and text2 in line:
                print(line)
                result.append(line)

search('Secure.log', 'Failed', '3187')
