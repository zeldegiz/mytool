from dns.resolver import resolve
from whois import whois
from ._except_handler import except_handler

class Scanner():
        def __init__(self,website):
            self.website = website
            
        @except_handler
        def A(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'A')))

        @except_handler    
        def AAAA(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'AAAA')))

        @except_handler
        def NS(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'NS')))

        @except_handler
        def CNAME(self):
            return list(map(lambda cname: cname.target, resolve(self.website,'CNAME')))

        @except_handler
        def MX(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'MX')))

        @except_handler
        def SOA(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'SOA')))

        @except_handler
        def TXT(self):
            return list(map(lambda ip: ip.to_text(), resolve(self.website,'TXT')))

        @except_handler
        def WHOIS(self):
            result = whois(self.website)
            return result if any(result.values()) else {}
