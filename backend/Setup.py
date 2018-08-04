import requests
from GoogleSearch import GoogleSearch

import prop


gs=GoogleSearch()
class Setup:

    os=['windows','mac','linux']
    USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



    def __init__(self):
        print('setup class')

    
    def makeRequest(self,url):
        res=requests.get(url, headers=self.USER_AGENT)

        return res

    def getDomainName(self,siteName):
        splitChunks=siteName.split('/')
        return splitChunks[2]




    def getOfficialWebsite(self,key):
        #link=res[0]['link']
        offiWebsiteRes=gs.search(key,1)
        offiDName=self.getDomainName(offiWebsiteRes[0]['link'])
        setUps=[]
        for o in self.os:
            searchQ='site:'+offiDName+' '+'set up on '+o
            setUps.append({o:gs.search(searchQ,3)})
        return setUps

    

    
# s=Setup()
# print(s.getOfficialWebsite('angular'))
            

    


