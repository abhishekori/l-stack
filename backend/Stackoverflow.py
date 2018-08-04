import requests
import json

class Stackoverflow:

    def __init__(self):
        print('Stackoverflow')

    def parseResponse(self,json):
        tags = []
        items = json['items']
        for item in items:
            tags.append(item['name'])
        return tags

    def callStackoverflow(self,query,number_results):
        # https://api.stackexchange.com/2.2/tags/typescript/related?page=1&pagesize=5&site=stackoverflow
        url = "https://api.stackexchange.com/2.2/tags/" + query + "/related?page=1&pagesize=" + str(number_results) + "&site=stackoverflow"
        response = requests.get(url)
        return response.text

    def getRelatedTags(self,query):
        response = self.callStackoverflow(query,5)
        relatedTags = self.parseResponse(json.loads(response))
        return relatedTags
