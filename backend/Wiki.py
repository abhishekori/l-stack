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
        wikiLink = queryResponse
        return wikiLink

    def getInfo(self,searchKey):
        summary = ""
        wikiLink = self.getWikiLink(searchKey)
        articleName = self.extractWikiArticleName(wikiLink[0]['link'])
        try:
            summary = wikipedia.summary(articleName)
        except Exception:
            summary = wikiLink[0]['description']
        return summary
