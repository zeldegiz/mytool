import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

class website_scanner():
    def __init__(self,url):
        # parse url to different part
        parsed_url = urlparse(url)
        # Check input url is correct or not , and if is not correct raise ValueError
        if(bool(parsed_url.netloc) and bool(parsed_url.scheme)): self.url = url 
        else: raise ValueError('Plase Enter Correct Url')
    
    def page_url_extracter(self,url):
        # Extract domain name from url
        domain_name = urlparse(url).scheme+"://"+urlparse(url).netloc
        # Send request to url and create html parser
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        # extracted a-href values and filter none values in html file
        extracted_urls = list(filter(None,[a_tag.attrs.get("href") for a_tag in soup.findAll("a")]))
        # change all relative urls to absolute urls
        extracted_urls = [urljoin(domain_name,url_) for url_ in extracted_urls]
        # Return unique urls 
        return set(extracted_urls)
        
    def crawler(self,max_url):
    
        urlqueue = {self.url}
        url_list = set()
        # If domain name start with www delete with part
        domain_name = urlparse(self.url).netloc[:3] if(urlparse(self.url).netloc[:3]=='www') else urlparse(self.url).netloc
            
        # While urlqueue is not empty and finded url is less than max wanted url, do operation
        while(len(urlqueue) and len(url_list)<max_url):
            # Extract urls in the link
            extracted_urls = self.page_url_extracter(urlqueue.pop())
            # Difference extracted_urls and url_list set for find not added urls and print
            extracted_urls -= url_list
            print(*extracted_urls,sep='\n')
            # Find internet urls
            internal_urls = set([url for url in extracted_urls if(domain_name in url)])
            # Union urlqueue and internal_urls
            urlqueue |= internal_urls
            # Union url_list and extracted_urls
            url_list |= extracted_urls