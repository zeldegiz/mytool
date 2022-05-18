'''
Scanner All Links in Website.
scan command for using start scanning.
'''
from ._website_scanner import website_scanner as _website_scanner
from pyfiglet import figlet_format as _figlet_format
def scan(url:str,max_url:int):
    
    '''
    Start Link Listing.

    
    Args:
        url (str): target url
        max_url (int): how many link will be found

    Return: None
    '''
    
    try:
        print(_figlet_format('Link Lister'))
        scanner = _website_scanner(url)
        scanner.crawler(max_url)
    except ValueError:
        print('Please Enter Correct url')
    except:
        pass