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
        self._configfile = configfile
        
    def is_config_available(self,configfile=''):
        if configfile == '':
            configfile = self._configfile
        if configfile != '' and os.access(self._configfile, os.F_OK):
            return 1
        else:
            return 0
        
    def load_conf(self):
        cfd = open(self._configfile,'r')
        
        def _start_element(name, attrs):
            global apposys,apponode,appoexe
            if name == 'system':
                apposys = system.System(attrs['systemname'],
                                        attrs['desc'],
                                        attrs['lastupd'])
            elif name == 'node':
                apponode = node.Node(attrs['hostname'],
                                     attrs['ip'],
                                     attrs['desc'],
                                     attrs['lastupd'])
            elif name == 'executable':
                appoexe = executable.Executable(attrs['execname'],
                                                attrs['path'],
                                                attrs['owner'],
                                                attrs['mode'],
                                                attrs['link'],
                                                attrs['desc'],
                                                attrs['lastupd'])
    
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
        cfd.close()
    
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
    
    def get_systems_list(self):
        return self._systems
            
    def save(self, configfile=''):
        if configfile != '':
            if os.access(configfile, os.F_OK):
                basefile, xmlext = os.path.splitext(configfile)
                shutil.move(configfile, basefile + '.bck')
            cfgf = configfile
        else:
            cfgf = self._configfile
        fc = open(cfgf, 'w')
        fc.write('<?xml version="1.0"?>\n')
        for sys in self._systems:
            line =           '<system systemname="' + sys.get_system_name()
            line = line + '"\n        desc="' + sys.get_system_description()
            line = line + '"\n        lastupd="' + sys.get_system_last_upd()
            line = line + '">\n'
            fc.write(line)
            for node in sys.get_system_node_list():
                line =           '  <node hostname="' + node.get_node_name()
                line = line + '"\n        ip="' + node.get_node_ip()
                line = line + '"\n        desc="' + node.get_node_description()
                line = line + '"\n        lastupd="' + node.get_node_last_upd()
                line = line + '">\n'
                fc.write(line)
                for exe in node.get_node_exec_list():
                    line =           '    <executable execname="' + exe.get_exec_name()
                    line = line + '"\n                path="' + exe.get_exec_location()
                    line = line + '"\n                owner="' + exe.get_exec_owner()
                    line = line + '"\n                mode="' + exe.get_exec_mode()
                    line = line + '"\n                link="' + exe.get_exec_link()
                    line = line + '"\n                desc="' + exe.get_exec_description()
                    line = line + '"\n                lastupd="' + exe.get_exec_last_upd()
                    line = line + '"/>\n'
                    fc.write(line)
                fc.write('  </node>\n')
            fc.write('</system>\n')
        fc.close()
