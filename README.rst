======
markov
======

Just a fun little experiment in producing Markov chains.

You really shouldn't use this, it's mostly just for me. Uses JSON for
serialization. Python 2.6+ or Python 3.3+.


Usage
=====

You can test the main code via::

    python markov.py

Which will dump out some text based on Python's `random`_ docs.

You can also test against some `Project Gutenberg`_ works, by first loading the
the data with::

    python guten_mark.py parse

Then producing a quote using::

    python guten_mark.py quote

.. _`random`: http://docs.python.org/3.3/library/random.html
.. _`Project Gutenberg`: http://www.gutenberg.org/ebooks/search/%3Fsort_order%3Ddownloads


License
=======

New BSD
