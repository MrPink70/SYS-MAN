'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
from subprocess import check_output
import os

def get_executable(execname, path):
    executable = Executable(execname, path)
    return executable
    
class Executable():
    '''A executable representation
    
    Attributes:
        
    '''

    def __init__(self, execname, path):
        '''
        Constructor
        '''
        self.filename = execname
        self.location = path
        self.fullname = path + os.sep + execname
        # controllare la presenza del file nel path
        # se l'eseguibile non viene trovato chiamare l'eccezione

    def get_CSCI_version(self):
        fullversion = check_output(['/usr/bin/ident', self.fullname]).splitlines()
        version = ''
        for line in fullversion:
            if line.find('CSCI') > -1: version = version + line.lstrip() + '\n'
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
    
    def is_versioned(self):
        version = self.get_EXEC_version().splitlines()
        if len(version) == 1:
            return 1
        else:
            return 0
        
if __name__ == '__main__':
    import glob
    path = str(raw_input('Inserisci il path degli eseguibili: '))
    listfile = glob.glob(path + '/E*3')
    print listfile
    for file in listfile:
        print '--------------------------------------------------------------------------------------'
        exfile = Executable(str(file).lstrip(path), path)
        if exfile.is_versioned():
            print 'L\'eseguibile e\' stato generato sotto controllo di configurazione'
        else:
            print 'L\'eseguibile e\' di linea'
        #print 'fullversion :\n' + exfile.get_CSCI_version()
        print 'versione    :\n' + exfile.get_EXEC_version()
        #print 'md5         :\n' + exfile.get_md5()
        #print 'sha1        :\n' + exfile.get_sha1()
        #print 'privilegi   :\n' + oct(exfile.get_privileges())
        #print 'proprietario:\n' + str(exfile.get_owner())
    print '--------------------------------------------------------------------------------------'        
