'''
Created on 07/mar/2012

@author: frosa
'''

from smerrors import *
from subprocess import check_output
import os

#def get_executable(execname, path, description=''):
#    executable = Executable(execname, path, description)
#    return executable
    
class Executable():
    '''A executable representation
    
    Attributes:
        
    '''

    def __init__(self, execname, path, owner, mode, link='', description='', lastupd='19880000000000'):
        '''
        Constructor
        '''
        self._filename = execname
        self._path = path
        self._location = path
        self._fullname = path + os.sep + execname
        self._owner = owner
        self._mode = mode
        self._link = link
        self._description = description
        self._lastupd = lastupd
        
    def __str__(self):
        return ('Executable ' + self._filename + '\n' +
                '  Located in ' + self._path + '\n' +
                '  Owned by ' + self._owner)

    def set_exec_description(self, description):
        '''
        Set the description of the Executable
        '''
        self._description = description
        
    def set_last_upd_time(self,lastupd):
        self._lastupd = lastupd
        
    def get_exec_name(self):
        '''
        Return the Executable name
        '''
        return self._filename
    
    def get_exec_short_name(self):
        '''
        Return the Executable 8 digit name
        '''
        return self._filename[0:8]
    
    def get_exec_owner(self):
        return self._owner
    
    def get_exec_mode(self):
        return self._mode
    
    def get_exec_link(self):
        return self._link
    
    def get_exec_description(self):
        '''
        Return the Ezecutable description
        '''
        return self._description
    
    def get_exec_last_upd(self):
        return self._lastupd
    
    def get_exec_location(self):
        return self._location
        
    def get_csci_version(self):
        '''
        Return a list of the Executable's components
        Equivalent to the shell command 'ident EXXXYYYN-MMRFCOOOO | grep CSCI' 
        '''
        fullversion = check_output(['/usr/bin/ident', self._fullname]).splitlines()
        version = ''
        for line in fullversion:
            if line.find('CSCI') > -1: version = version + line.lstrip() + '\n'
        return version.rstrip('\n')
    
    def get_version(self):
        fullversion = self.get_csci_version().splitlines()
        version = ''
        for line in fullversion:
            if line.find(self._filename[0:8]) > -1: version = version + line + '\n'
        return version.rstrip('\n')
    
    def get_short_version(self):
        return str(self.get_version()).lstrip('$CSCIrevision: ').rstrip(' $')
    
    def get_os_version(self):
        fullversion = self.get_csci_version().splitlines()
        version = ''
        for line in fullversion:
            if line.find('CSCIoperativesystem') > -1: version = version + line + '\n'
        return version.rstrip('\n')
    
    def get_os_short_version(self):
        return str(self.get_os_version()).lstrip('$CSCIoperativesystem: ').rstrip(' $')
    
    def get_md5(self):
        md5code = check_output(['/usr/bin/md5sum', self._fullname])
        return md5code.rstrip('\n')
    
    def get_sha1(self):
        sha1code = check_output(['/usr/bin/sha1sum', self._fullname])
        return sha1code.rstrip('\n')
 
    def get_privileges(self):
        statexecfile = os.stat(self._fullname).st_mode
        return statexecfile
    
    def get_owner(self):
        statexecfile = os.stat(self._fullname).st_uid
        return statexecfile
    
    def is_versioned(self):
        version = self.get_exec_version().splitlines()
        if len(version) == 1:
            return 1
        else:
            return 0

#if __name__ == '__main__':
#    import glob
#    #path = str(raw_input('Inserisci il path degli eseguibili: '))
#    path = '/home/frosa/APPO'
#    path = '/home/fabrizio/Test/SYS-MAN/APPO'
#    listfile = glob.glob(path + '/E*3')
#    print listfile
#    for file in listfile:
#        print '--------------------------------------------------------------------------------------'
#        print str(file)
#        exfile = Executable(str(file).lstrip(path), path, 'root', '100')
#        if exfile.is_versioned():
#            print 'L\'eseguibile e\' stato generato sotto controllo di configurazione'
#        else:
#            print 'L\'eseguibile e\' di linea'
#        #print 'fullversion :\n' + exfile.get_CSCI_version()
#        print 'versione    :\n' + exfile.get_exec_version()
#        #print 'md5         :\n' + exfile.get_md5()
#        #print 'sha1        :\n' + exfile.get_sha1()
#        print 'privilegi   :\n' + oct(exfile.get_privileges())
#        print 'proprietario:\n' + str(exfile.get_owner())
#    print '--------------------------------------------------------------------------------------'        