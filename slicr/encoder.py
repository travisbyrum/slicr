# -*- coding: utf-8 -*-

"""
slicr.encoder
~~~~~~~~~~~~~
Encoder module to turn urls in base64 encoded strings.

:copyright: © 2018
"""


ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class UrlEncoder:
    """Base url encoder."""

    def __init__(self, alphabet=ALPHABET, salt=0):
        """Url encoder to convert numeric id values to new bases.

        :param alphabet: Set of characters for use in creating short urls,
            defaults to ALPHABET
        :param alphabet: str, optional
        :param salt: Salt value to create unique ids, defaults to 0
        :param salt: int, optional
        """

        self._alphabet = alphabet
        self._base = len(alphabet)
        self._salt = salt

    def encode(self, url_id):
        """Convert numeric id to hash id based on alphabet.

        :param url_id: Value id.
        :type url_id: int
        """

        if url_id <= 0:
            raise ValueError('Id must be greater than zero.')

        url_id = url_id + self._salt

        short_url = ''
        while url_id > 0:
            digit_remainder = url_id % self._base
            short_url += self._alphabet[digit_remainder]
            url_id = url_id // self._base

        return short_url

    def decode(self, short_url):
        """Convert hashed id back into numeric id.

        :param short_url: Hashed id value.
        :type short_url: str
        """

        url_id = 0
        for index, digit in enumerate(short_url):
            url_id += self._alphabet.find(digit) * int(self._base ** index)

        return url_id - self._salt
