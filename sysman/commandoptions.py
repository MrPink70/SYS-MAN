'''
Created on Mar 27, 2012

@author: frosa
'''
from optparse import OptionParser
import sysman

class Commandoptions():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        parser = OptionParser(usage='usage: %prog [Option]',
            version=('SysMan Version: ' + (sysman.version())))
        parser.add_option('-p',
            '--port',
            dest='port',
            default='61874',
            help='the port on which to host the SysMan server. Default: 61874')
        parser.add_option('-f',
            '--file',
            dest='conffile',
            default='/home/frosa/APPO/sysman.xml',
            help='the configuration file. Default: /home/frosa/APPO/sysman.xml')
        (self.options,self.args) = parser.parse_args()
