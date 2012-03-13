

class System():
    def __init__(self, sysName, nodeList, sysDescr = ''):
        self.name = sysName
        self.nodes = nodeList
        self.description = sysDescr

    def set_description(self, sysDescr):
        self.description = sysDescr