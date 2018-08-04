from GoogleSearch import GoogleSearch
import wikipedia

class Wiki:

    def __init__(self):
        print("Wiki class")

    def extractWikiArticleName(self,link):
        #https://en.wikipedia.org/wiki/Angular_(application_platform)
        return link[30:].replace("_"," ")

    def getWikiLink(self,searchQuery):
        googleSearch = GoogleSearch()
        query = searchQuery + "Wiki"
        queryResponse = googleSearch.search(query,1)
        wikiLink = queryResponse[0]['link']
        return wikiLink

    def getInfo(self,searchKey):
        wikiLink = self.getWikiLink(searchKey)
        articleName = self.extractWikiArticleName(wikiLink)
        return wikipedia.summary(articleName)
