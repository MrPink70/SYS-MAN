'''
Created on Mar 23, 2012

@author: frosa
'''
import socket,thread,re,cPickle

import sysman.confhandler

class Server():
    '''
    classdocs
    '''

    def __init__(self,port,configfile):
        '''
        Constructor
        '''
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(('',int(port)))
        self._port = port
        self._configfile = configfile
        self._mutex=thread.allocate_lock()
        self._commandlist = ['help',
                             'load_conf:<sysname>',
                             'is_conf_available',
                             'status',
                             'set_conf',
                             'update']
        self._config = sysman.confhandler.Configuration(self._configfile) 
        self._sock.listen(2)
        try:
            while True:
                conn, addr = self._sock.accept()
                thread.start_new_thread(self._handle_connection,(conn,addr[0]))
        except:
            print "Exception occured!"
        self.stop()
        
    def _handle_connection(self,conn,addr):
        cd = conn.makefile()
        for command in cd:
            comm = re.sub('[\n\r]','',command)
            match = re.match('^(.+):(.+)$',comm)
            if match:
                req = match.group(1)
                print req
                par = match.group(2)
                with self._mutex:
                    if req == 'help':
                        resp = str(self._commandlist)
                    elif req == 'load_conf':
                        systemname = par
                        resp = cPickle.dumps(self._config.get_system(systemname))
                    elif req == 'is_conf_available':
                        resp = self._config.is_config_available()
                    elif req == 'status':
                        resp = 'Status'
                    elif req == 'set_conf':
                        for line in cd:
                            line = re.sub('[\n]','',line)
                            if line == '*DONE':
                                line =  cd.readline()
                                break
                            par += '\n%s' % line
                        system = cPickle.loads(par)
                        self._config.add_system(system)
                        self._config.save()
                        resp = 'Config added'
                    elif req == 'update':
                        resp = 'Update'
                    else:
                        resp = 'Invalid Order Received'
                    cd.write('%s\n*DONE\n' % resp)                    
                    cd.flush()
            else:
                with self._mutex:
                    cd.write('Invalid order received\n*DONE\n')
                    cd.flush()
        conn.close()
    
    def stop(self):
        self._sock.close()