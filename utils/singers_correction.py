def correct_singers_file(name='singers.txt'):
    singers = list(set(open(name).read().split('\n')))
    singers.sort()
    with open (name, 'w') as f:
        f.write('\n'.join(singers))
