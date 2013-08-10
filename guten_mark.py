from __future__ import print_function
import glob
import random
import sys

from markov import Markov


def parse(mark):
    for filename in glob.glob('guten/*.txt'):
        with open(filename, 'r') as guten_file:
            for line in guten_file.readlines():
                # Skip blank lines.
                if not line.strip():
                    continue

                mark.parse(line)

    mark.save()


def quote(mark):
    mark.load()
    sentences = []

    for i in range(random.randint(3, 8)):
        sentences.append(mark.say())

    return u' '.join(sentences)


if __name__ == '__main__':
    mark = Markov(filename='gutenberg.json')

    if len(sys.argv) < 2:
        print("Usage: guten_mark.py (parse|say)")
        sys.exit(1)

    if sys.argv[1] == 'parse':
        parse(mark)
    elif sys.argv[1] == 'quote':
        print(quote(mark))
    else:
        print("Unrecognized flag '{0}'".format(sys.argv[1]))
        sys.exit(1)
