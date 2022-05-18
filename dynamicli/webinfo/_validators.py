import enum
import re

class Commands(enum.Enum):
    A = 'A'
    AAAA = 'AAAA'
    NS = 'NS'
    CNAME = 'CNAME'
    MX = 'MX'
    SOA = 'SOA'
    TXT = 'TXT'
    WHOIS = 'WHOIS'
    
    @classmethod
    def check(cls , value):
        return value in cls._value2member_map_

def commandsvalidator(commands:tuple) -> bool:
    return all(map(Commands.check,commands))
    
def websitevalidator(website:str):
    wb_pattern = re.compile(r'(www\.)?[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    return wb_pattern.match(website)