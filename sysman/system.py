

class System():
    def __init__(self, sysName, description='', lastupd='19880000000000'):
        self._name = sysName
        self._nodelist = []
        self._description = description
        self._lastupd = lastupd

    def set_description(self, description):
        self._description = description
        
    def set_last_upd_time(self,lastupd):
        self._lastupd = lastupd
        
    def insert_system_node(self, node):
        self._nodelist.append(node)
        
    def remove_system_node(self, nodename):
        for node in self._nodelist:
            if str(node.get_node_name()) == nodename:
                self._nodelist.remove(node)

    def get_system_name(self):
        return str(self._name)
    
    def get_system_description(self):
        return str(self._description)
    
    def get_system_last_upd(self):
        return self._lastupd

    def get_system_node_list(self):
        return self._nodelist




#if __name__ == '__main__':
#    from executable import *
#    from node import *
#    #path = '/home/Subang/APPO'
#    path = '/home/fabrizio/Test/SYS-MAN/APPO'
#    system1 = System('Subang', 'Subang system')
#    node1 = Node('D01', 'Controller Working Position')
#    node2 = Node('BN1', 'Best Node Server')
#    exfile = get_executable('EA20IKS1-10RFCRHEL3', path, 'IKS')
#    node1.insert_node_exec(exfile)
#    exfile = get_executable('E0R1XSD1-01RFCRHEL3', path, 'SMD')
#    node1.insert_node_exec(exfile)
#    node2.insert_node_exec(exfile)
#    exfile = get_executable('E000IKM0-01RFCRHEL3', path, 'IKM')
#    node2.insert_node_exec(exfile)
#    system1.insert_system_node(node1)
#    system1.insert_system_node(node2)
#    print 'System: ' + system1.get_system_name() + ' (' + system1.get_system_description() + ')'
#    for node in system1.get_system_node_list():
#        print '--------------------------------------------------'
#        print '  Node: ' + node.get_node_name() + ' (' + node.get_node_description() + ')'
#        print '    Exec list:'
#        for exe in node.get_node_exec_list():
#            print '      ' + str(exe.get_exec_version()).lstrip('$CSCIrevision: ').rstrip(' $')
#            print '        ' + str(exe.get_exec_os_version()).lstrip('$CSCIoperativesystem: ').rstrip(' $')
#    print '--------------------------------------------------'
#    print 'Removing D01 node'
#    system1.remove_system_node('D01')
#    print 'D01 node removed'
#    for node in system1.get_system_node_list():
#        print '--------------------------------------------------'
#        print '  Node: ' + node.get_node_name() + ' (' + node.get_node_description() + ')'
#        print '    Exec list:'
#        for exe in node.get_node_exec_list():
#            print '      ' + str(exe.get_exec_version()).lstrip('$CSCIrevision: ').rstrip(' $')
#            print '        ' + str(exe.get_exec_os_version()).lstrip('$CSCIoperativesystem: ').rstrip(' $')

    