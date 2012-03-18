'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
from subprocess import check_output
import os
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
        self.fullname = path + os.sep + execname
        # controllare la presenza del file nel path
        # se l'eseguibile non viene trovato chiamare l'eccezione

    def get_CSCI_version(self):
        fullversion = check_output(['/usr/bin/ident', self.fullname]).splitlines()
        version = ''
        for line in fullversion:
            if line.find('CSCI') > -1: version = version + line.lstrip() +'\n'
        return version.rstrip('\n')
    
    def get_EXEC_version(self):
        fullversion = self.get_CSCI_version().splitlines()
        version = ''
        for line in fullversion:
            if line.find(self.filename[0:8]) > -1: version = version + line + '\n'
        return version.rstrip('\n')
    
    def get_md5(self):
        md5code = check_output(['/usr/bin/md5sum', self.fullname])
        return md5code.rstrip('\n')
    
    def get_sha1(self):
        sha1code = check_output(['/usr/bin/sha1sum', self.fullname])
        return sha1code.rstrip('\n')
 
    def get_privileges(self):
        statexecfile = os.stat(self.fullname).st_mode
        return statexecfile
    
    def get_owner(self):
        statexecfile = os.stat(self.fullname).st_uid
        return statexecfile
    
if __name__ == '__main__':
    exfile = Executable('E000XTH0-01RFCRHEL3', '/home/fabrizio')
    print 'fullversion :\n' + exfile.get_CSCI_version()
    print 'versione    :\n' + exfile.get_EXEC_version()
    print 'md5         :\n' + exfile.get_md5()
    print 'sha1        :\n' + exfile.get_sha1()
    print 'privilegi   :\n' + oct(exfile.get_privileges())
    print 'proprietario:\n' + str(exfile.get_owner())