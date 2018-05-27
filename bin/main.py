#!/usr/bin/env python

"""
Created May 25, 2018

@author: Travis Byrum
"""

import argparse

from slicr import create_app
from slicr.config import Config


def main():
    """Application entrypoint."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help='Slicr port number.',
        default=5000
    )
    parser.add_argument(
        '--host',
        type=str,
        help='Slicr host address.',
        default='0.0.0.0'
    )
    parser.add_argument(
        '-d',
        '--debug',
        type=bool,
        help='Enable debugging.',
        default=True
    )

    args = parser.parse_args()
    print(args)

    app = create_app(config=Config, args=args.debug)

    app.run(host=args.host, port=args.port, threaded=True)


if __name__ == '__main__':
    main()
