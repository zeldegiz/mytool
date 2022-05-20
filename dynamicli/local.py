'''
Using for finding local ip addresses.
mine command return your own ip address in local network.
devicelist command return all devices in local network with ip and mac address.
monitor command monitor tcp package on network.
'''
import socket
from scapy.all import sniff as _sniff, Ether as _Ether, ARP as _ARP, srp as _srp
from pyfiglet import figlet_format as _figlet_format

def mine() -> str:
    '''
    Find Your IP Address in Local Network
    
    Args:
        None
        
    Return: str
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as st:
        st.connect(('8.8.8.8', 1))
        ip_address = st.getsockname()[0]
        print(f'Computer IP Address is: {ip_address}')
    return ip_address
    
def devicelist(timeout: int,iter_size:int) -> None:
    '''
    Find All Devices in Local Network with IP and MAC Addresses
    
    Args:
        timeout (int):  packet max waiting value
        iter_size (int): how many times send ARP requests
    
    Return: None
    '''
    try:
        print(figlet_format('Device Lister'))
        ip_address = mine()
        request = ARP()
        request.pdst = f'{ip_address}/24'
        broadcast = Ether()
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
        # Get ARP request iter_size time and collect information as nested list
        clients_lists = [srp(broadcast / request, timeout = timeout)[0] for i in range(iter_size)]
        # Use Nested List comprehension for take parameters from requests
        client_list = [(client[1].psrc,client[1].hwsrc) for lists in clients_lists for client in lists]
        # Find unique Clients with set 
        unique_clients = set(client_list)
        print(f'Find {len(unique_clients)} clients in local network')
        # Extract ip and mac address as string from clients
        ip_mac_list = [f'{ip_add.center(20)}:{mac_add.center(20)}' for ip_add,mac_add in unique_clients]
        print(*ip_mac_list,sep='\n')
    except Exception as e:
        print('Error Occurred')
        print(e)

def monitor(size:int) -> None:
    '''
    Monitor TCP Package on Local Network
    
    Args:
        size (int): how many packet held
        
    Return: None
    '''
    print(_figlet_format('Local Network Monitor'))
    # find division and mod
    div,mod = divmod(size,5)
    try:
        # Declare function for print package information
        printer = lambda packet: print(f'{packet[0][1].src}:{packet[0][1].sport} -> {packet[0][1].dst}:{packet[0][1].dport}')
        # sniff 5 packet for division time
        for i in range(div):
            _sniff(filter="tcp", prn=printer , count=5)
        # sniff mod packet if mod packet is not 0, if it is 0, do not anything
        _sniff(filter="tcp", prn=printer , count=mod) if(mod) else None
    except:
        pass
