'''
Scanner open ports in server.
scan command for using start scanning ports to target ip.
'''
import socket
from threading import Thread as _Thread, Lock as _Lock
from ._iterable_queue import IterableQueue as _IterableQueue
def scan(host:str , start_port:int , end_port:int ,thread:int) -> None:
    
    '''
    Start Port Scanning.

    
    Args:
        host (str): target ip
        start_port (int): start port value
        end_port (int): end port value
        thread (int): how many thread use
    
    Return: None
    '''
    
    q = _IterableQueue()
    lock = _Lock()
    port_list = _IterableQueue()
    def scan_port(port):
        try:
            s = socket.socket()
            s.connect((host, port))
        except:
            with lock:
                print(f"{host}:{port} is closed")
        else:
            with lock:
                print(f"{host}:{port} is opened")
            port_list.put(port)
        finally:
            s.close()
    
    def scan_thread():
        while(True):
            worker = q.get()
            scan_port(worker)
            q.task_done()
            
    for i in range(thread):
        t = _Thread(target=scan_thread)
        t.daemon = True
        t.start()
    for port in range(start_port,end_port): q.put(port)
    try:
        q.join()
        print('Finded Ports',*[f'Port : {port}' for port in port_list],sep='\n') if(port_list) else print(f"Didn't Find Any Opened Port")
    except:
        pass