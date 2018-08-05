import requests
import json
import re, math
from collections import Counter

class Suggestions:

    def __init__(self):
        print("suggestions")

    def get_cosine(vec1, vec2):
         intersection = set(vec1.keys()) & set(vec2.keys())
         numerator = sum([vec1[x] * vec2[x] for x in intersection])

         sum1 = sum([vec1[x]**2 for x in vec1.keys()])
         sum2 = sum([vec2[x]**2 for x in vec2.keys()])
         denominator = math.sqrt(sum1) * math.sqrt(sum2)

         if not denominator:
            return 0.0
         else:
            return float(numerator) / denominator

    WORD = re.compile(r'\w+')

    def text_to_vector(text):
         words = WORD.findall(text)
         return Counter(words)


    def getSuggestions(self,sentence):
        cosineScores = []
        cosines = {}
        suggestions = []
        #https://api.stackexchange.com/2.2/search?order=desc&sort=activity&site=stackoverflow&intitle=what%20is%20angular
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&site=stackoverflow&intitle=" + sentence
        response = requests.get(url)
        jsonResponse = json.loads(response.text)
        items = jsonResponse['items']
        for item in items:
            cosine = get_cosine(text_to_vector(sentence),text_to_vector(item['title']))
            cosineScores.append(cosine)
            cosines[cosine] = item

        cosineScores.sort(reverse=True)
        for x in range(5):
            score = cosineScores[x]
            suggestion = {}
            suggestion['rank'] = (x + 1)
            suggestion['question'] = cosines[score]['title']
            suggestion['link'] = cosines[score]['link']
            suggestions.append(suggestion)

        return suggestions
