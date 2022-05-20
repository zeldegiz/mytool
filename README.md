# CLI Tool for Pentesting

	Please read before use!
    
    For Linux users only and can use DOCKERFILE 
    Works with python version >= 3.9
    Install requirements in requirements.txt via pip3.
    Make the "mytool" file executable using linux terminal typing `chmod +x compute` command
    
## Example
```
# ./mytool -h
usage: mytool [-h] [-v] {local,scanner,webinfo} ...

positional arguments:
  {local,scanner,webinfo}
    local               Using for finding local ip addresses. mine command return your own ip address in local
                        network. devicelist command return all devices in local network with ip and mac address.
                        monitor command monitor tcp package on network.
    scanner             Scanner command for using scan website. linklister command for using take all links in
                        website. adminfinder command for using find admin panel url. portscanner command for using
                        find open ports in server.
    webinfo             Using for Collecting Information About Website. find command for using start collecting
                        information.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

```
# ./mytool local devicelist 3 3
 ____             _            _     _     _
|  _ \  _____   _(_) ___ ___  | |   (_)___| |_ ___ _ __
| | | |/ _ \ \ / / |/ __/ _ \ | |   | / __| __/ _ \ '__|
| |_| |  __/\ V /| | (_|  __/ | |___| \__ \ ||  __/ |
|____/ \___| \_/ |_|\___\___| |_____|_|___/\__\___|_|


Computer IP Address is: 192.168.65.3
Begin emission:
Finished sending 256 packets.
***
Received 3 packets, got 3 answers, remaining 253 packets
Begin emission:
Finished sending 256 packets.
***
Received 3 packets, got 3 answers, remaining 253 packets
Begin emission:
Finished sending 256 packets.
***
Received 3 packets, got 3 answers, remaining 253 packets
Find 3 clients in local network
    192.168.65.2    : f6:16:36:bc:f9:c6
    192.168.65.3    : 02:50:00:00:00:01
    192.168.65.1    : f6:16:36:bc:f9:c6
 ```
## Project layout
```
├── dynamicli
   ├── scanner
   │   ├── __init__.py
   │   ├── _file_reader.py 
   │   ├── _iterable_queue.py
   │   ├── _website_scanner.py
   │   ├── adminfinder.py
   │   ├── linklister.py
   |   ├── portscanner.py
   |   ├── urls.txt
   ├── webinfo
   |   ├── __init__.py
   |   ├── _except_handler.py
   |   ├── _validators.py
   |   ├── _webinfo.py
   ├── local.py
   ├── mytool
```
### Contains:
```
Admin Panel Link Finder 
Backlink Lister
Open Port Scanner
Website Investigator
Local Network Device Lister
Local Network sniffing Tool
Own IP address finder
 ``` 

Built on top of DynaCLI by BST Labs. [Check it out!](https://github.com/BstLabs/py-dynacli)
