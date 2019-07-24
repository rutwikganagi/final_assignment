import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
        thepage = urllib.request.urlopen(url)
        soupdata = BeautifulSoup(thepage,"html.parser")
        return soupdata

playerdatasaved=""
soup=make_soup("https://karki23.github.io/Weather-Data/BadgerysCreek.html")
#Similarly scraping all other tables

flag=0;

for record in soup.findAll("tr"):
    playerdata=""
    if flag==0:
            for data in record.findAll("th"):
                    playerdata=playerdata+","+data.text
                    flag=1
            playerdatasaved = playerdatasaved + "\n" +playerdata[1:]
            continue
    for data in record.findAll("td"):
        playerdata=playerdata+","+data.text
    playerdatasaved = playerdatasaved + "\n" +playerdata[1:]
    

file = open(os.path.expanduser("BadgerysCreek.csv"),"wb")

file.write(bytes(playerdatasaved,encoding="ascii",errors="ignore"))


