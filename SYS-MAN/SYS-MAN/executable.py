'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
class executable():
    '''A executable representation
    
    Attributes:
        
    '''


    def __init__(self, triliteral, execname):
        '''
        Constructor
        '''
        if len(triliteral) == 3:
            self.triliteral = triliteral
        else:
            raise NameLengthError(triliteral, 'name must be 3 character')
        self.filename = execname
        
        