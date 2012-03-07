class NameLengthError(Exception):
    """Exception raised for wrong name length.
    
    Attributes:
        value -- the string passed with wrong length
        msg   -- explanation of the error
    """
    def __init__(self, value, msg):
        self.value = value
        self.msg = msg