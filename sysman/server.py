'''
Created on Mar 23, 2012

@author: frosa
'''
import socket,thread,re

class Server():
    '''
    classdocs
    '''

    def __init__(self,port):
        '''
        Constructor
        '''
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(('',int(port)))
        self._sock.listen(2)
        print 'Socket in LISTEN'
        self._port = port
        self._mutex=thread.allocate_lock()
        self._commandlist = ['help','stop']
        try:
            while True:
                conn, addr = self._sock.accept()
                # break off a thread to handle the connection
                thread.start_new_thread(self._handle_connection,(conn,addr[0]))
        except:
            print "Exception occured!"
        self._sock.close()
        
    def _handle_connection(self,conn,addr):
        cd = conn.makefile()
        for req in cd:
            print 'Reading QUERY'
            req = re.sub('[\n\r]','',req)
            with self._mutex:
                if req == 'help':
                    print 'received HELP command'
                    cd.write(str(self._commandlist) + '\n')
                elif req == 'stop':
                    print 'Received STOP command'
                    conn.close()
                    raise Exception('STOP')
                cd.write('*DONE\n')
                cd.flush()
        conn.close()
        print 'Connection CLOSED'
                    