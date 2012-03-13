'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
class Executable():
    '''A executable representation
    
    Attributes:
        
    '''

    def __init__(self, triliteral, execname, version):
        '''
        Constructor
        '''
        if len(triliteral) == 3:
            self.triliteral = triliteral
        else:
            raise NameLengthError(triliteral, 'name must be 3 character')
        self.filename = execname

    def get_local_version(self):
        pass
    
    def get_remote_version(self):
        pass