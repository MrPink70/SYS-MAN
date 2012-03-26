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
        self._lock=thread.allocate_lock()
        self._addr = addr
        self._port = port
        
    def query(self,req):
        with self.lock():
            #get the file
            cd=self.socket().makefile()
            #send the query
            cd.write('%s\n' % req)
            cd.flush()
            info=''
            #read until final token
            for line in cd:
                #get rid of excess newline
                line=re.sub('\n','',line)
                if line == '*DONE':
                    #it's over
                    break
                #append the line
                info += '%s\n' % line
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

