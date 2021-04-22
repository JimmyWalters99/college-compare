import os 
import io
import gzip
import sys
import urllib
import urllib3
import urllib.parse
import urllib.request
import re

from bs4 import BeautifulSoup


def download_page(url):
    return urllib.request.urlopen(url)

def didYouMean(q):
    q = str(str.lower(q)).strip()
    url = "http://www.google.com/search?q=" + urllib.parse.quote_plus(q)
    html = download_page(url)
    soup = BeautifulSoup(html)
    ans = soup.find('a', attrs={'class' : 'spell'})
    try:
        result = repr(ans.contents)
        result = result.replace("u'","")
        result = result.replace("/","")
        result = result.replace("<b>","")
        result = result.replace("<i>","")
        result = re.sub('[^A-Za-z0-9\s]+', '', result)
        result = re.sub(' +',' ',result)
    except AttributeError:
        result = 1
    return result

if __name__ == "__main__":
    response = didYouMean('babon colleeg')
    print(response)