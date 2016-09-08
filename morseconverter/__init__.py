import codecs
import sys

__author__ = 'Gokhan MANKARA'
__email__ = 'gokhan@mankara.org'
__version__ = '0.1'

pyver = sys.version_info >= (3, 0)

if pyver:
    sys_input = sys.stdin
else:
    UTF8Reader = codecs.getreader('utf8')
    sys_input = UTF8Reader(sys.stdin)
