# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import re
import random


__author__ = 'Daniel Lindsley'
__license__ = 'New BSD'


class Markov(object):
    def __init__(self, filename='markov.json', max_words=15):
        super(Markov, self).__init__()
        self.filename = filename
        self.max_words = max_words
        self.words = {}
        self.cleaner = re.compile(r'[^\w\s]')

    def load(self):
        with open(self.filename, 'r') as json_file:
            self.words = json.load(json_file)

    def save(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self.words, json_file, indent=2)

    def clean(self, word):
        # Removes punctuation & whitespace.
        return self.cleaner.sub('', word.strip().lower())

    def parse(self, message):
        # Break up the words in the message.
        words = message.split(' ')

        if len(words) > 2:
            # Then pass a moving window (3 words wide) over the words.
            # The first two become a key, the third gets added to a list of
            # words that appear after those previous two.
            for offset in range(len(words) - 2):
                word_1 = self.clean(words[offset])
                word_2 = self.clean(words[offset + 1])
                word_3 = self.clean(words[offset + 2])

                key = u' '.join([word_1, word_2])
                self.words.setdefault(key, [])
                self.words[key].append(word_3)

    def say(self):
        # Generate a sentence from 2 to 15 words long.
        word_count = random.randint(1, self.max_words)
        # We need a starting point, so grab a random key.
        # Painful on memory, but whatever.
        current = random.choice(list(self.words.keys()))
        response = current.split(u' ')

        for i in range(word_count):
            try:
                choice = random.choice(self.words[current])
            except IndexError:
                break
            except KeyError:
                break

            response.append(choice)
            current = u' '.join([response[-2], choice])

        # Create a bytestring (because Unicode strings don't have a
        # ``.capitialize()`` method...).
        raw_sentence = u' '.join(response).encode('utf-8')

        try:
            raw_sentence = raw_sentence.captialize()
        except:
            pass

        raw_sentence = raw_sentence.decode('utf-8')
        # Add on random punctuation, so they read more naturally.
        raw_sentence += random.choice(['.', ',', '.', '?', '.'])
        return raw_sentence


if __name__ == '__main__':
    messages = [
        u'This module implements pseudo-random number generators for various distributions.',
        u'For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.',
        u'Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.',
        u'The functions supplied by this module are actually bound methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state.',
        u'Initialize the random number generator.',
        u'If a is omitted or None, the current system time is used. If randomness sources are provided by the operating system, they are used instead of the system time (see the os.urandom() function for details on availability).',
    ]

    mark = Markov()

    for message in messages:
        mark.parse(message)

    mark.save()

    mark_2 = Markov()
    mark_2.load()

    for i in range(5):
        print(mark_2.say())
