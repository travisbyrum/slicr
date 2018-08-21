# -*- coding: utf-8 -*-

"""
slicr.models
~~~~~~~~~~~~
Model definitions and schemas.

:copyright: © 2018
"""

from .domains import Domain, DomainSchema
from .links import Link, LinkSchema


__all__ = ['Domain', 'DomainSchema', 'Link', 'LinkSchema']
