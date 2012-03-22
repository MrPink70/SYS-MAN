'''
Created on Mar 22, 2012

@author: frosa
'''
import xml.parsers.expat,os
from sysman import system,node,executable

class Configuration():
    '''
    classdocs
    '''

    def __init__(self, configfile):
        '''
        Constructor
        '''
        self._systems = []
        if os.access(configfile, os.F_OK):
            cf = open(configfile,'r')
            self._load_conf(cf)
            
    def _load_conf(self,cfd):
        
        def _start_element(name, attrs):
            global apposys,apponode,appoexe
            if name == 'system':
#                print '+--System: ' + attrs['systemname'] + ' (' + attrs['desc'] + ') ' + ' last update: ' + attrs['lastupd']
                apposys = system.System(attrs['systemname'], attrs['desc'], attrs['lastupd'])
            elif name == 'node':
#                print '|  +--Node: ' + attrs['hostname'] + ' (' + attrs['desc'] + ') ' + attrs['lastupd']
                apponode = node.Node(attrs['hostname'], attrs['desc'], attrs['lastupd'])
            elif name == 'executable':
#                print '|  |  +--Exec: ' + attrs['execname'] + ' in ' + attrs['path'] +' (' + attrs['desc'] + ') ' + attrs['lastupd']
                appoexe = executable.Executable(attrs['execname'], attrs['path'], attrs['desc'], attrs['lastupd'])
    
        def _end_element(name):
            global apposys,apponode,appoexe
            if name == 'system':
                self._systems.append(apposys)
            elif name == 'node':
                apposys.insert_system_node(apponode)
            elif name == 'executable':
                apponode.insert_node_exec(appoexe)
    
        def _char_data(data):
            pass
        config = xml.parsers.expat.ParserCreate()
        config.StartElementHandler = _start_element
        config.EndElementHandler = _end_element
        config.CharacterDataHandler = _char_data
        config.ParseFile(cfd)
    
    def get_system(self, systemname):
        for sys in self._systems:
            if sys.get_system_name() == systemname:
                return sys
        