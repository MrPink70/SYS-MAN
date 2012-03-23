'''
Created on Mar 22, 2012

@author: frosa
'''
import xml.parsers.expat,os,shutil
from sysman import system,node,executable

class Configuration():
    '''
    classdocs
    '''

    def __init__(self, configfile=''):
        '''
        Constructor
        '''
        self._systems = []
        if configfile != '' and os.access(configfile, os.F_OK):
            cf = open(configfile,'r')
            self.load_conf(cf)
            cf.close()
            
    def load_conf(self,cfd):
        
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
    
    def add_system(self, sys):
        self._systems.append(sys)
        
    def remove_system(self, systemname):
        for sys in self._systems:
            if sys.get_system_name() == systemname:
                self._systems.remove(sys)
                
    def get_system(self, systemname):
        for sys in self._systems:
            if sys.get_system_name() == systemname:
                return sys
            
    def save(self, configfile):
        if configfile != '':
            if os.access(configfile, os.F_OK):
                basefile, xmlext = os.path.splitext(configfile)
                shutil.move(configfile, basefile + '.bck')
            fc = open(configfile, 'w')
            fc.write('<?xml version="1.0"?>\n')
            for sys in self._systems:
                line ='<system systemname="' + sys.get_system_name() + \
                '" desc="' + sys.get_system_description() + \
                '" lastupd="' + sys.get_system_last_upd() + \
                '">\n'
                fc.write(line)
                for node in sys.get_system_node_list():
                    line = '  <node hostname="' + node.get_node_name() + \
                    '" desc="' + node.get_node_description() + \
                    '" lastupd="' + node.get_node_last_upd() + \
                    '">\n'
                    fc.write(line)
                    for exe in node.get_node_exec_list():
                        line = '    <executable execname="' + exe.get_exec_name() + \
                        '" path="' + exe.get_exec_location() + \
                        '" desc="' + exe.get_exec_description() + \
                        '" lastupd="' + exe.get_exec_last_upd() + \
                        '"/>\n'
                        fc.write(line)
                    fc.write('  </node>\n')
                fc.write('</system>\n')
            fc.close()