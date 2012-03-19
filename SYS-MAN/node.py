'''
Created on 06/mar/2012

@author: frosa
'''

from executable import *
from smerrors import *
class Node:
    '''A node representation.
    
    Attributes:
        name -- hostname, default = NOD
    '''
    def __init__(self, nodename='NOD'):
        if len(nodename) == 3:
            self.name = nodename
        else:
            raise NameLengthError(nodename, 'name must be 3 character')
        self.execlist = []
        
    def insert_exec(self, exeobj):
        self.execlist.append(exeobj)
        
    def get_exc_version_list(self):
        exclist = self.execlist
        verslist = []
        for ex in exclist:
            verslist.append(ex.get_EXEC_version())
        return verslist

    def update(self):
        '''
        Update all the available executables of the node
        ''' 
        pass

if __name__ == '__main__':
    #path = str(raw_input('Inserisci il path degli eseguibili: '))
    #exna = str(raw_input('Inserisci il nome dell\'eseguibile: '))
    #exfile = Executable(str(exna), path)
    exfile = get_executable('EA20XTA1-01RFCRHEL3', '/home/fabrizio/Test/SYS-MAN/APPO')
    print exfile.get_EXEC_version()
    node1 = Node('D01')
    print 'Nome Nodo: ' + node1.name
    node1.insert_exec(exfile)
    verslist = node1.get_exc_version_list()
    for vers in verslist:
        print 'Versione: ' + str(vers)
    #try:
    #    node2 = Node('PIPPO')
    #except NameLengthError as ex:
    #    print 'Handle exception: "' + ex.value + '" ' + ex.msg
    #node3 = Node()
    #print node3.name

