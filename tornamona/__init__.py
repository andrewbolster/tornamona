"""Top-level package for Tornamona."""

__author__ = """Andrew Bolster"""
__email__ = 'me@andrewbolster.info'
__version__ = '0.1.2'

import logging
import sys

log = logging.getLogger('Tornamona')
log.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stream_handler)
from tornamona.fixes import nisra
