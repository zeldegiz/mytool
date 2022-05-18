'''
Using for Find admin panel url.
start command for using start scanning.
'''
import validators , requests
from pyfiglet import figlet_format as _figlet_format
from ._file_reader import read_generator as _read_generator
 
def start(url:str,delay:float) -> None:
    '''
    Start Admin Panel Scanning.

    
    Args:
        url (str): target url
        delay (int): delay second for each request

    Return: None
    '''   
    print(_figlet_format('Admin Finder'))
    
    # Validate user input is correct url form
    if(not validators.url(url)):
        print('Please Enter Correct URL')
        return
    path = 'scanner/urls.txt'
    # Take base url from input url
    url = '/'.join(url.split('/')[:3])+'/'
    headers={'User-Agent':'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}
    
    try:
       '''Do get request to link from read_generator generator, which create possibly admin links. If response status 
        is 200, then this link is available,then print and return url , else only print url
        '''
       result = [(print(f'{url_} : 200'),url_)[1] if(requests.get(url_,headers=headers).status_code == 200) \
        else print(f'{url_} : 404') for url_ in _read_generator(path,url,delay)]
       '''use filter function for filter None value,because if response didn't return 200 status code,then only print and 
       print function return None value
       '''
       finded_links = list(filter(None,result))
       print('Finded Links'),print(*finded_links,sep='\n') if(finded_links) else print('Didn\'t Find Any Link')
    except:
        pass