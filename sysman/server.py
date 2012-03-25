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
                             'update',
                             'stop']
        self._config = sysman.confhandler.Configuration(self._configfile) 
        self._sock.listen(2)
        try:
            while True:
                conn, addr = self._sock.accept()
                print 'assign connection parameters'
                # break off a thread to handle the connection
                thread.start_new_thread(self._handle_connection,(conn,addr[0]))
                print 'starting thread'
        except:
            print "Exception occured!"
        self.stop()
        
    def _handle_connection(self,conn,addr):
        print 'start handle_connection'
        cd = conn.makefile()
        print 'create file descriptor'
        for command in cd:
            comm = re.sub('[\n\r]','',command)
            print 'strip LF CR'
            match = re.match('^(.+):(.+)$',comm)
            print 'separate received token'
            req = match.group(1)
            print 'assigne request %s' % req
            par = match.group(2)
            print 'assigne parameter %s' % par
            with self._mutex:
                if req == 'help':
                    cd.write('%s\n' % str(self._commandlist))
                elif req == 'load_conf':
                    systemname = par
                    cd.write('%s\n' % cPickle.dumps(self._config.get_system(systemname)))
                    pass
                elif req == 'is_conf_available':
                    cd.write('%s\n' % self._config.is_config_available())                    
                elif req == 'status':
                    pass
                elif req == 'set_conf':
                    print 'in set_conf'
                    match = re.match('^(.+):(.+)$',command)
                    print 'matching'
                    par = match.group(2)
                    print par
                    system = cPickle.loads(par)
                    print 'load system'
                    self._config.add_system(system)
                    print 'adding system'
                    self._config.save('/home/fabrizio/APPO/ucraina.xml')
                    print 'saving configuration'
#                    cd.write('Config added\n')
                elif req == 'update':
                    pass
                elif req == 'stop':
                    cd.write('Received STOP command\n*DONE\n')
                    cd.flush()
                    conn.close()
                    thread.exit()
                else:
                    cd.write('Invalid order received\n')
                cd.write('*DONE\n')
                cd.flush()
        conn.close()
    
    def stop(self):
        self._sock.close()