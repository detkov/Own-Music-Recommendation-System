import sys

def correct_singers_file(filename='singers.txt'):
    # filename = '../' + filename
    singers = list(set(open(filename).read().split('\n')))
    singers.sort()
    with open (filename, 'w') as f:
        f.write('\n'.join(singers))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        correct_singers_file()
        pass
    else:
        filename = sys.argv[1]
        correct_singers_file(filename=filename)
        pass