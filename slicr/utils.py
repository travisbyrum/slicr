# -*- coding: utf-8 -*-

"""
slicr.utils
~~~~~~~~~~~
Utility functions and helpers.

:copyright: © 2018
"""

from collections import namedtuple


def convert_args(args_dict):
    """Convert dictionary to named tuple enabling class like attribute access.

    :param args_dict: Dictionary of arguments to convert.
    :type args_dict: dict
    :return: Named tuple of arguments.
    :rtype: collections.namedtuple
    """

    return namedtuple(
        typename='arguments',
        field_names=args_dict.keys()
    )(**args_dict)
