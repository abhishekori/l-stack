import requests
from bs4 import BeautifulSoup
from flask import jsonify


import prop

class Setup:

    os=['windows','mac','linux']
    USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


    def __init__(self):
        print('setup class')

    
    def makeRequest(self,url):
        res=requests.get(url, headers=self.USER_AGENT)
        return res



    def getOfficialWebsite(self,key,number_results):
        escaped_search_term = key.replace(' ', '+')
        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, 'en')
        reqObj = self.makeRequest(google_url)
        res=self.parse_results(reqObj.text,key)
        link=res[0]['link']
        return link

    def parse_results(self,html, keyword):
        soup = BeautifulSoup(html, 'html.parser')
        found_results = []
        rank = 1
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:

            link = result.find('a', href=True)
            title = result.find('h3', attrs={'class': 'r'})
            description = result.find('span', attrs={'class': 'st'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                if link != '#':
                    found_results.append({'link':link,'keyword': keyword, 'rank': rank, 'title': title, 'description': description})
                    rank += 1
        return found_results

    
# s=Setup()
# print(s.getOfficialWebsite('angular wiki',1))
            

    


