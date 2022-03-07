import json
from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "http://cfcunderwriting.com"

def readurl(url):
    website = urlopen(url)
    read_site = website.read()
    soup = BeautifulSoup(read_site, "html.parser")
    return soup

# print(readurl(url))




def external_res():
    soup = readurl(url)
    res = {"img":"src", "script":"src", "video":"src", "audio":"src", "iframe":"src", "embed":"src", "object":"data", "source":"src", "font-face":"src"}
    with open("externals.json", "r+") as j:
        json_object = json.load(j)
        for items in res: 
            tag = items
            attribute = res[items]
            
            for x in soup.findAll(tag):
                    if "http" in str(x):
                        try:
                            json_object["List"][0][tag].append(x[attribute])
                        except KeyError:
                            pass
            j.seek(0)
            json.dump(json_object, j, indent=2)
# external_res()





def find_privacy(url): 
    privacy_link = ""
    soup = readurl(url)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    
    for i, items in enumerate(links):
            if items != None and "privacy" in items:
                privacy_link = url + items
                print(f'Privacy policy is hyperlink number {i} with the url: {privacy_link}')
                break

# find_privacy(url)

def frequency_count(): 
    soup = readurl(url)
    with open("Wordcount.json","r+") as z:
        Json_object = json.load(z)
        for words in soup.get_text().split():
                if words.lower() in Json_object["List"][0]:
                    Json_object["List"][0][words.lower()] +=1
                else:   
                    Json_object["List"][0][words.lower()] = 1
        z.seek(0)
        json.dump(Json_object, z, indent=2)

frequency_count()