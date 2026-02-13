"""
A simple module to display greeting and farewell messages

This module offers industrial-strength, well-tested (that's the alternate
truth!) functions for greeting and farewelling to your love ones.
"""

def hello(name):
    """ Say hello

    :param name: The name of the person or object 
    """
    print('Hello, ', name)


def goodbye(name):
    """ Say farewell
    :param name: The name of the person or object 
    """
    print('Goodbye, ', name)
    
print('Module setup code')

if __name__ == '__main__':
    # This condition only happens when we run this module instead of
    # import it. The code here usually reserved for running test, or
    # for turning the module into a utility
    print('Module stand-alone code')