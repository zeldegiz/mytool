'''
Using for Collecting Information About Website.
find command for using start collecting information.
'''
from pyfiglet import figlet_format
from ._webinfo import Scanner
from ._validators import commandsvalidator,websitevalidator

def find(website: str,*commands: str) -> None:
    '''
    Start Collect Information About Target Website.
    Command List: A , AAAA , NS , CNAME , MX , SOA , TXT , WHOIS
    
    Args:
        website (str): target website
        commands (str): commands list
    
    Return: None
    '''
    
    if(not commandsvalidator(commands) or len(commands)==0):
        print('Please use only correct commands') if(commands) \
        else print('Please use at least one command')
        
    elif(websitevalidator(website)):
        print(figlet_format('Website Informer'))
        print(f'Scanned website: {website}')
        
        scanner = Scanner(website)
        results = [getattr(scanner,command)() for command in commands]
        for command,result in zip(commands,results):
            print('-'*50)
            print(f'{command} Result')
            print(result) if(result) else print('Didn\'t find anything')
            
    else:
        print('Website didn\'t correct')