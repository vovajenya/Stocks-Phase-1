import bs4 as bs
import urllib.request
import requests
import browse_dynamic_web as dynamic

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'


def spider(web_page, url, word, dynamic_page):

    all_links = list()
    all_titles = list()
    opener = AppURLopener()

    # soup = urllib.request.urlopen(url)
    word = make_list(word)
    try:
        if dynamic_page:
            response = dynamic.fetch(url,5)
        else:
            response = opener.open(url)

        soup = bs.BeautifulSoup(response, 'lxml')

        for link in soup.find_all('a'):
            # if word in link.text:
            link_str = link.text
            if any(w in link_str for w in word):
                all_titles.append(link.text)
                if 'http' in link.attrs['href']: # direct link
                    all_links.append(link.attrs['href'])

                else: # article
                    all_links.append(web_page + link.attrs['href'])

        return all_links, all_titles

    except:
        return list()

def make_list(string):
    # this function will return a list after splitting the string to words
    if isinstance(string, str):
        return string.split()

    return string
