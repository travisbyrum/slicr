"""
Created June 27, 2018

@author: Travis Byrum
"""

from slicr.utils import convert_args


def test_convert_args():
    """Convert dictionary of arguments to namedtuple."""

    arg_dict = {
        'key_one': 'test',
        'key_two': 1,
        'key_three': True
    }

    args = convert_args(arg_dict)

    assert args.key_one == 'test'
    assert args.key_two == 1
    assert bool(args.key_three)
