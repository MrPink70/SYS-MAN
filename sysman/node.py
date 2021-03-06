'''
Created on 06/mar/2012

@author: frosa
'''

from smerrors import *
class Node:
    '''A node representation.
    
    Attributes:
        name -- hostname, default = NOD
    '''
    def __init__(self, nodename, ip, description='', lastupd='19880000000000'):
#        if len(nodename) == 3:
#            self._name = nodename
#        else:
#            raise NameLengthError(nodename, 'name must be 3 character')
        self._name = nodename
        self._ip = ip
        self._description = description
        self._lastupd = lastupd
        self._execlist = []
        
    def __str__(self):
        return ('Node ' + self._nodename + '\n' +
                '  IP ' + self._ip)
        
    def set_node_description(self, description):
        self._description = description
    
    def set_last_upd_time(self,lastupd):
        self._lastupd = lastupd
        
    def insert_node_exec(self, exeobj):
        self._execlist.append(exeobj)
    
    def remove_node_exec(self, exename):
        for exe in self._execlist:
            if str(exe.get_exec_name()) == exename:
                self._execlist.remove(exe)
    
    def get_node_name(self):
        return str(self._name)
        
    def get_node_ip(self):
        return self._ip
    
    def get_node_description(self):
        return str(self._description)
    
    def get_node_last_upd(self):
        return self._lastupd

    def get_node_exec_version_list(self):
        verslist = []
        for exe in self._execlist:
            verslist.append(exe.get_exec_version())
        return verslist
    
    def get_node_exec_list(self):
        return self._execlist

    def update(self):
        '''
        Update all the available executables of the node
        ''' 
        pass




#if __name__ == '__main__':
#    from executable import get_executable
#    #path = '/home/Subang/APPO'
#    path = '/home/fabrizio/Test/SYS-MAN/APPO'
#    exfile = get_executable('EA20IKS1-10RFCRHEL3', path)
#    node1 = Node('D01')
#    print 'Nome Nodo: ' + node1.get_node_name()
#    node1.insert_node_exec(exfile)
#    verslist = node1.get_node_exec_version_list()
#    print '--------------------------------------------------------------'
#    for vers in verslist:
#        print 'Versione: ' + str(vers)
#    exfile = get_executable('E0R1XSD1-01RFCRHEL3', path)
#    node1.insert_node_exec(exfile)
#    verslist = node1.get_node_exec_version_list()
#    print '--------------------------------------------------------------'
#    for vers in verslist:
#        print 'Versione: ' + str(vers)
#    node1.remove_node_exec('EA20IKS1-10RFCRHEL3')
#    verslist = node1.get_node_exec_version_list()
#    print '--------------------------------------------------------------'
#    for vers in verslist:
#        print 'Versione: ' + str(vers)
    
    #try:
    #    node2 = Node('PIPPO')
    #except NameLengthError as ex:
    #    print 'Handle exception: "' + ex.value + '" ' + ex.msg
    #node3 = Node()
    #print node3.name

