# Sometimes it is helpful to be able to reduce a large piece of data
# down to a smaller piece for purposes of verification or error-checking.
#
# Given a data source (a large block of text, a large data file, etc)
# it is possible to construct an artifical "digest" of that data
# in such a way so that even a small change in the source would result
# in a large, obvious change in the digest.
#
# These digests are therefore useful in "identifying" the original data source.
# They are therefore often called "hashes" or "digital fingerprints"
# and form the basis for all of our online security today.
#
# There are many algorithms that can achieve a desired result
# with various levels of robustness and speed.
#
# https://docs.python.org/3.5/library/hashlib.html#module-hashlib
#
# Let's explore the MD5 and SHA-2 algorithms.

import hashlib
