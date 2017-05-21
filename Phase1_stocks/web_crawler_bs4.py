import bs4 as bs
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def spider(web_page, url, word):


    all_links = list()

    opener = AppURLopener()
    response = opener.open(url)
    soup = bs.BeautifulSoup(response,'lxml')

    for link in soup.find_all('a'):
        if word in link.text:
            if 'http' in link.attrs['href']: # direct link
                all_links.append(link.attrs['href'])
            else: # article
                all_links.append(web_page + link.attrs['href'])

    return all_links