'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
class Executable():
    '''A executable representation
    
    Attributes:
        
    '''

    def __init__(self, execname, path):
        '''
        Constructor
        '''
#        if len(triliteral) == 3:
#            self.triliteral = triliteral
#        else:
#            raise NameLengthError(triliteral, 'name must be 3 character')
        self.filename = execname
        self.location = path
        # controllare la presenza del file nel path
        # se l'eseguibile non viene trovato chiamare l'eccezione

    def get_version(self):
        pass
    
    def get_mda5(self):
        pass
    
    def get_sha1(self):
        pass
 
    def get_privileges(self):
        pass
    
    def get_owner(self):
        pass