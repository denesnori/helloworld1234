"""
A hello world module
"""

import sys

__version__ = '0.0.2'


def hello(name='World'):
    """
      Return a greeting for a given name.
    """
    return 'Hello, {}'.format(name)


def main():
    """
      Reads input from the args passed into
      the script and prints the output to
      stdout.
    """
    args = sys.argv[1:]
    name = ' '.join(args)
    if name:
        print(hello(name))
    else:
        print(hello())


if __name__ == '__main__':
    main()
