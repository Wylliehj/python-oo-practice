"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize 2 variables, 1 to store the start value and 1 to act as a counter"""
        self.start = start
        self.next = start

    def generate(self):
        """Return the next serial number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset serial number to original start value"""
        self.next = self.start


