from GoogleSearch import GoogleSearch
import settings
import json
gs=GoogleSearch()

class MOOC:


    def __init__(self):
        print('MOOC class')


    def getMoocs(self,key):

        res=[]

        for m in settings.settings['moocs']:
            searchQuery='site:'+m+' '+key
            res.append({m:gs.search(searchQuery,3)})
        return res

    


# m=MOOC()
# print(json.dumps(m.getMoocs('python'),indent=2, sort_keys=True))




        


    


