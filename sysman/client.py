'''
Created on Mar 23, 2012

@author: frosa
'''

import socket,thread,re

class Client():
    '''
    classdocs
    '''

    def __init__(self,addr,port):
        '''
        Constructor
        '''
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((addr,port))
        print 'Socket CONNECTED'
        self._lock=thread.allocate_lock()
        self._addr = addr
        self._port = port
        
    def query(self,req):
        print 'Start querying'
        with self.lock():
            #get the file
            f=self.socket().makefile()
            #send the query
            f.write('%s\n' % req)
            f.flush()
            info=''
            #read until final token
            for line in f:
                #get rid of excess newline
#                print line
                line=re.sub('\n','',line)
                if line == '*DONE':
                    #it's over
                    break
                #append the line
                info += '%s\n' % line
            print 'End querying'
            return info
        
    def socket(self):
        """Returns the backing socket.
        
        Because using this socket erases the thread safety, this
        method should never be used.
        """
        return self._sock

    def lock(self):
        """Returns the backing lock.
        """
        return self._lock

    def acquire(self):
        """Calls acquire on the backing lock.
        """
        self._lock.acquire()

    def release(self):
        """Releases the backing lock.
        """
        self._lock.release()
    
    def addr(self):
        """Returns the remote address in use.
        """
        return self._addr

    def port(self):
        """Returns the remote port in use.
        """
        return self._port

