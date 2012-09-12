""" Collection of pynmea specific errors
"""

class NoDataGivenError(Exception):
    def __init__(self, message):
        self.message = message

class ChecksumException(Exception):
    pass

class TMQException(Exception):
    pass