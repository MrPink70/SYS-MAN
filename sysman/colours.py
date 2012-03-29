'''
Created on Mar 29, 2012

@author: frosa
'''
END = '\033[0m'
BOLD = '\033[1m'
UNDERL = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
B_RED = '\033[41m'
B_GREEN = '\033[42m'
B_YELLOW = '\033[43m'
B_BLUE = '\033[44m'
B_MAGENTA = '\033[45m'
B_CYAN = '\033[46m'

def red_bold(text):
    text = BOLD + RED + text + END
    return text

def yellow_bold(text):
    text = BOLD + YELLOW + text + END
    return text

def blue_bold(text):
    text = BOLD + BLUE + text + END
    return text

def green_bold(text):
    text = BOLD + GREEN + text + END
    return text

def bold(text):
    text = BOLD  + text + END
    return text

def green_bold_reverse(text):
    text = BOLD + GREEN + REVERSE + ' ' + text + ' ' + END
    return text