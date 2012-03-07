from smerrors import *
class Node:
    """A node representation.
    
    Attributes:
        nodename -- hostname, default = NOD
    """
    def __init__(self, nodename='NOD'):
        if len(nodename) == 3:
            self.name = nodename
        else:
            raise NameLengthError(nodename, 'name must be 3 character')


if __name__ == '__main__':
    node1 = Node('D01')
    print node1.name
    try:
        node2 = Node('PIPPO')
    except NameLengthError as ex:
        print 'Handle exception: "' + ex.value + '" ' + ex.msg
    node3 = Node()
    print node3.name

