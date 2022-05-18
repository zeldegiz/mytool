# mytool
Mytool is command line tool offer some pentest tools for local network, investigate website information and  scanning. This tool created dynacli package. You can use this tool for using dockerfile or upload dynamicli folder some linux distibution and install all requirement libraries which listed in requirements.txt.

## Local Command
Local command for using run some function for local network <br>
If you want see your ip in local network use : `./mytool local mine` <br>
<br>
![](https://i.postimg.cc/1RgyWgpv/screenshot-484.png) <br>
<br>
If you want see all ip's in local network, then use : `./mytool local devicelist <timeout> <iter-size>` <br>
timeout value is waiting time to packet and iter-size is value of how many times send request <br><br>
![](https://i.postimg.cc/BvDxcZmb/screenshot-485.png) <br><br>
If you want sniffing local network, then use : `./mytool local monitor <size>` <br>
size value is indicates how many packet will sniffing <br><br>
![](https://i.postimg.cc/YqYGsD1D/screenshot-486.png) <br><br>

## Webinfo Command
Webinfo command for using collect information about website <br>
For this command use `./mytool webinfo find <website> <commandlist>` <br>
Command List is A , AAAA , NS , CNAME , MX , SOA , TXT , WHOIS <br><br>
![](https://i.postimg.cc/XvM20zhZ/screenshot-487.png) <br><br>

## Scanner Command
Scanner command for using scan websites and servers for find admin panel, extract all links in website and find open ports
If you want find website admin panel, then use `./mytool scanner adminfinder start <website> <delay>` <br>
Website value is target website and delay value is using for add waiting time each request <br><br>
![](https://i.postimg.cc/g0J3Qqcw/screenshot-488.png) <br><br>
If you want extract all links in website, then use `./mytool scanner linklister scan <url> <max_url>` <br>
Url value is target url and max_url determine how many url extracted <br><br>
![](https://i.postimg.cc/vZm1ZYJk/screenshot-489.png) <br><br>
If you want find opened ports in website or server, then use `./mytool scanner portscanner scan <host> <start_port> <end_port> <thread>` <br>
Host value is target website or ip address, start_port and end_port are determine range of port, thread value is use for how many thread using <br><br>
![](https://i.postimg.cc/15KnS6z2/screenshot-490.png)
